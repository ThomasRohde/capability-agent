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
  --tasks 4 \
  --override-system-message examples/system.txt \
  --context-level full_tree,parent,siblings \
  --context-format markdown \
  --log-prompts logs/ \
  --streaming \
  --restart
```

### Key Options

- `--restart`: Resume generation from input file, updating it in place (ignores `--output` option)
- `--streaming`: Use streaming API for real-time progress (requires `--tasks 1`)
- `--log-prompts`: Directory to save rendered prompts for debugging/analysis
- `--context-format`: Context output format (json, markdown, or xml)
- `--context-level`: Include context types (full_tree, parent, siblings)

Environment:
- Set `OPENAI_API_KEY` for API access.

## Features

- **Concurrent Processing**: Parallel LLM calls with configurable task count
- **Restart Capability**: Resume interrupted augmentation processes from existing files
- **Streaming Support**: Real-time progress with OpenAI streaming API
- **Flexible Context**: Multiple context formats and levels for prompting
- **Prompt Logging**: Save rendered prompts for debugging and analysis
- **Progress Tracking**: Rich terminal UI with real-time progress bars
- **Atomic Updates**: Safe file operations with data integrity guarantees

## Notes
- Input and output are strict JSON arrays of nodes. Extra fields are preserved.
- IDs must be unique UUID4 strings; new children are assigned after model generation.
- On any validation or IO error, the CLI prints a clear message and exits code 1.
- Use restart functionality to resume long-running augmentation processes safely.
