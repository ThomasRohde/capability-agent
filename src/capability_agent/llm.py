from __future__ import annotations

import json
import os
from typing import Dict, List

from openai import OpenAI


class LLMError(Exception):
    pass


def _extract_json_array(text: str) -> str | None:
    """Extract the first top-level JSON array substring from text.

    Handles code fences and ignores brackets inside quoted strings.
    Returns the JSON array string or None if not found.
    """
    # Fast path: strip code fences
    if "```" in text:
        parts = text.split("```")
        for i in range(1, len(parts), 2):
            block = parts[i]
            # remove an optional language tag on first line
            if "\n" in block:
                block_body = block.split("\n", 1)[1]
            else:
                block_body = block
            if "[" in block_body and "]" in block_body:
                text = block_body
                break

    s = text
    start = s.find("[")
    if start == -1:
        return None
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(s)):
        ch = s[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        else:
            if ch == '"':
                in_str = True
                continue
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    return s[start : i + 1]
    return None


def ensure_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("Environment variable OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)


def call_openai(client: OpenAI, system_message: str, user_prompt: str, max_items: int) -> List[Dict[str, str]]:
    """Call OpenAI Responses API and return a list of {name, description} dicts.

    Uses Responses API with strict JSON schema to enforce structured output.
    """
    # Strict schema for an array of capability items
    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "capability_items",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "name": {"type": "string", "minLength": 1},
                        "description": {"type": "string", "minLength": 1},
                    },
                    "required": ["name", "description"],
                },
            },
            "strict": True,
        },
    }

    model = os.getenv("OPENAI_MODEL") or "gpt-5-nano"
    try:
        resp = client.responses.create(
            model=model,
            # temperature=0.3,
            instructions=system_message,
            input=user_prompt,
            response_format=response_format,
        )
    except TypeError as e:
        # Older SDKs may not support response_format on Responses API; retry without it
        if "response_format" in str(e):
            # Append JSON format instruction to ensure JSON output when structured output fails
            json_instruction = "\n\nIMPORTANT: Return ONLY a JSON array with objects containing 'name' and 'description' fields. Example: [{\"name\": \"...\", \"description\": \"...\"}]"
            try:
                resp = client.responses.create(
                    model=model,
                    # temperature=0.3,
                    instructions=system_message + json_instruction,
                    input=user_prompt,
                )
            except Exception as e2:  # noqa: BLE001
                raise LLMError(f"OpenAI API error: {e2}") from e2
        else:
            raise LLMError(f"OpenAI API error: {e}") from e
    except Exception as e:  # noqa: BLE001
        raise LLMError(f"OpenAI API error: {e}") from e

    # Prefer convenience property; fallback to assembling text if needed
    content_text = getattr(resp, "output_text", None)
    if not content_text:
        # Attempt to reconstruct text from the response object
        try:
            # responses API returns a list of output items; concatenate any text parts
            chunks: List[str] = []
            for out in getattr(resp, "output", []) or []:
                for part in getattr(out, "content", []) or []:
                    if getattr(part, "type", None) == "output_text":
                        text = getattr(getattr(part, "text", {}), "value", "")
                        if text:
                            chunks.append(text)
            content_text = "".join(chunks)
        except Exception:  # noqa: BLE001
            content_text = ""

    if not content_text:
        raise LLMError("Model returned empty response text.")

    # Extract JSON array robustly (handles fences and extra text)
    json_text = _extract_json_array(content_text) or content_text

    try:
        data = json.loads(json_text)
        if not isinstance(data, list):
            raise ValueError("Expected a JSON array at top level")
    except Exception as e:  # noqa: BLE001
        raise LLMError(
            "Model output was not valid JSON array. Parse error: "
            f"{e}\nRaw: {content_text}"
        ) from e

    items: List[Dict[str, str]] = []
    for item in data[:max_items]:
        if not isinstance(item, dict):
            raise LLMError("Each generated item must be an object.")
        name = item.get("name")
        desc = item.get("description")
        
        # Check if parent field is present (shouldn't be, but might cause confusion)
        if "parent" in item:
            # Ignore parent field but log warning for debugging
            pass  # Parent should not be in LLM output
        
        if not isinstance(name, str) or not isinstance(desc, str):
            raise LLMError("Each item must have string 'name' and 'description' fields.")
        items.append({"name": name, "description": desc})
    return items
