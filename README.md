# capability-agent / business-capgen

A Python CLI to augment a business capability model: reads a JSON array of nodes, renders Jinja2 prompts per leaf, calls OpenAI to propose sub-capabilities, validates with Pydantic, and writes an augmented JSON array.

## Install

Use pipx (recommended) for a global command install:

```sh
pipx install .
```

Or local editable install:

```sh
pip install -e .
```

## Usage

```sh
business-capgen \
  --input examples/model.json \
  --template examples/prompt.j2 \
  --output out.json \
  --max-capabilities 5 \
  --override-system-message examples/system.txt \
  --context-level full_tree,parent,siblings
```

Environment:
- Set `OPENAI_API_KEY` for API access.

## Notes
- Input and output are strict JSON arrays of nodes. Extra fields are preserved.
- IDs must be unique UUID4 strings; new children are assigned after model generation.
- On any validation or IO error, the CLI prints a clear message and exits code 1.
