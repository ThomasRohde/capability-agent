from __future__ import annotations

import json
import os
from typing import Dict, List

from openai import OpenAI


class LLMError(Exception):
    pass


def ensure_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("Environment variable OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)


def call_openai(client: OpenAI, system_message: str, user_prompt: str, max_items: int) -> List[Dict[str, str]]:
    try:
        resp = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt},
            ],
        )
    except Exception as e:  # noqa: BLE001
        raise LLMError(f"OpenAI API error: {e}") from e

    content = resp.choices[0].message.content or ""

    # Extract possible JSON from markdown code fences
    json_text = content
    if "```" in content:
        parts = content.split("```")
        if len(parts) >= 2:
            for i in range(1, len(parts), 2):
                block = parts[i]
                if block.strip().startswith("json"):
                    json_text = block.split("\n", 1)[1] if "\n" in block else "[]"
                    break
            else:
                json_text = parts[1]

    try:
        data = json.loads(json_text)
        if not isinstance(data, list):
            raise ValueError("Expected a JSON array")
    except Exception as e:  # noqa: BLE001
        raise LLMError(f"Model output was not valid JSON array. Parse error: {e}\nRaw: {content}") from e

    items: List[Dict[str, str]] = []
    for item in data[:max_items]:
        if not isinstance(item, dict):
            raise LLMError("Each generated item must be an object.")
        name = item.get("name")
        desc = item.get("description")
        if not isinstance(name, str) or not isinstance(desc, str):
            raise LLMError("Each item must have string 'name' and 'description' fields.")
        items.append({"name": name, "description": desc})
    return items
