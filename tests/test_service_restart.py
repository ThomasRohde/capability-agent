import json
import uuid

import pytest

from capability_agent.io_utils import ContextFormat, ContextOptions
from capability_agent.llm import UsageStats
from capability_agent.models import CapabilityList
from capability_agent.service import augment_model


def test_restart_progress_persists_children(tmp_path, monkeypatch):
    root_id = str(uuid.uuid4())
    leaf_a_id = str(uuid.uuid4())
    leaf_b_id = str(uuid.uuid4())

    model_data = [
        {
            "id": root_id,
            "name": "Root",
            "description": "Root description",
            "parent": None,
            "capability": 0,
        },
        {
            "id": leaf_a_id,
            "name": "Leaf A",
            "description": "Leaf A description",
            "parent": root_id,
            "capability": 0,
        },
        {
            "id": leaf_b_id,
            "name": "Leaf B",
            "description": "Leaf B description",
            "parent": root_id,
            "capability": 0,
        },
    ]

    input_path = tmp_path / "model.json"
    input_path.write_text(json.dumps(model_data), encoding="utf-8")

    template_path = tmp_path / "template.j2"
    template_path.write_text("Prompt for {{ node.name }}", encoding="utf-8")

    model = CapabilityList.model_validate(model_data)

    fake_client = object()
    monkeypatch.setattr("capability_agent.service.ensure_client", lambda *args, **kwargs: fake_client)

    usage_stats = UsageStats(model_name="fake", input_tokens=1, output_tokens=1, total_tokens=2)

    call_count = {"value": 0}

    def fake_call_openai(client, system_message, user_prompt, max_capabilities):
        call_count["value"] += 1
        if call_count["value"] == 1:
            return ([{"name": "Generated Child", "description": "Child description"}], usage_stats)
        raise RuntimeError("boom")

    monkeypatch.setattr("capability_agent.service.call_openai", fake_call_openai)
    def unexpected_stream(*args, **kwargs):  # pragma: no cover - defensive guard
        raise AssertionError("streaming not expected during test")

    monkeypatch.setattr("capability_agent.service.call_openai_streaming", unexpected_stream)

    with pytest.raises(RuntimeError):
        augment_model(
            model=model,
            template_path=template_path,
            context_opts=ContextOptions(),
            context_format=ContextFormat.MARKDOWN,
            system_message="system",
            max_capabilities=1,
            tasks=1,
            log_prompts_dir=None,
            use_streaming=False,
            restart_mode=True,
            input_path=input_path,
            openai_log_dir=None,
            openai_log_level="none",
        )

    saved = json.loads(input_path.read_text(encoding="utf-8"))

    # Leaf A should now be marked complete and have a generated child persisted.
    leaf_a = next(node for node in saved if node["id"] == leaf_a_id)
    assert leaf_a.get("capability") == 1

    generated_children = [node for node in saved if node.get("parent") == leaf_a_id]
    assert generated_children, "Generated child missing from persisted progress"
    assert generated_children[0]["name"] == "Generated Child"

    # Leaf B should be marked for retry with the captured error.
    leaf_b = next(node for node in saved if node["id"] == leaf_b_id)
    assert leaf_b.get("capability") == -1
    assert leaf_b.get("error") == "boom"
