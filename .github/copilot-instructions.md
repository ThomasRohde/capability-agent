## Copilot instructions for capability-agent (business-capgen)

Purpose: a CLI that augments a flat JSON array of business capability nodes by generating sub-capabilities for each leaf via an LLM, validating with Pydantic, and writing an augmented JSON array.

Architecture (start here):
- Entry point CLI: `src/capability_agent/cli.py` using Typer. Console script: `business-capgen` (see `pyproject.toml`).
- Orchestration: `augment_model` in `src/capability_agent/service.py`
	- Finds leaves (`CapabilityList.leaves()`), builds prompt context per leaf, renders a Jinja2 template, calls the LLM, then creates new child nodes.
	- Extra fields on input nodes are preserved and inherited to generated children, except reserved: `id`, `name`, `description`.
- Prompting: `src/capability_agent/prompting.py`
	- `build_prompt_context(model, node, ContextOptions)`: provides `node`, optional `parent`, `siblings`, and optional `full_tree` depending on flags.
	- `render_prompt(template_path, context)`: Jinja2 with `StrictUndefined`, `trim_blocks`, `lstrip_blocks`.
- LLM integration: `src/capability_agent/llm.py`
	- `ensure_client()` requires `OPENAI_API_KEY`; optional `OPENAI_MODEL` (default `gpt-4o-mini`).
	- `call_openai(client, system_message, user_prompt, max_items)`: uses Chat Completions, expects a JSON array in the model’s reply (optionally inside ```json fences); validates each item has string `name` and `description`.
- Data model: `src/capability_agent/models.py`
	- `Capability` (Pydantic v2) with UUID4 `id`, `name`, `description`, optional `parent`; `extra="allow"` to keep unknown fields.
	- `CapabilityList` (RootModel[List[Capability]]): ensures unique IDs; helpers `by_id()`, `children_map()`, `leaves()`.
- IO/utilities: `src/capability_agent/io_utils.py`
	- JSON read/write, default system message, and `parse_context_level("full_tree,parent,siblings")` to `ContextOptions`.

How to run (developer smoke test):
- Install (Python >= 3.10): `pipx install .` or `pip install -e .`
- Set `OPENAI_API_KEY`. Optional: `OPENAI_MODEL`.
- PowerShell example using bundled samples:
	business-capgen `
		--input examples/model.json `
		--template examples/prompt.j2 `
		--output enhanced_model.json `
		--max-capabilities 5 `
		--override-system-message examples/system.txt `
		--context-level full_tree,parent,siblings

Contracts and conventions (don’t break):
- Input and output are strict JSON arrays of nodes (not a nested tree). New children get `parent` set to the source leaf’s `id` and a new UUID4 `id`.
- Preserve unknown fields end-to-end; children inherit parent’s extra fields except `id`, `name`, `description`.
- Prompt templates must render without undefined vars (Jinja2 `StrictUndefined`). See `examples/prompt.j2` and `examples/system.txt`.
- CLI errors must print a clear message (Rich) and exit code 1 (`typer.Exit(1)`), as in `cli.run`.

Extension points (patterns seen in code):
- New CLI option: add a `typer.Option` in `cli.run`, validate/parse in `io_utils` if it’s a context-like flag, pass through to `service.augment_model`.
- Alternate LLMs: implement a function with the same return type as `call_openai(...)-> List[Dict[name,description]]`, or branch in `llm.call_openai` on an env var; keep the JSON-array output contract.
- Node schema changes: update `Capability` and adjust inheritance in `service.augment_model` to preserve extras while handling any new required fields.

Troubleshooting (common):
- Missing API key: `LLMError: Environment variable OPENAI_API_KEY is not set.`
- Bad context flags: `parse_context_level` raises `ValueError` for unknown options.
- Model output parse failures: `Model output was not valid JSON array...`; ensure the template instructs the model to return a JSON array inside ```json fences.

Key files to read first: `src/capability_agent/service.py`, `src/capability_agent/cli.py`, `src/capability_agent/llm.py`, `src/capability_agent/models.py`, `examples/*`.

Feedback welcome: if any workflow or convention here is unclear or incomplete, point it out so we can refine this guide.

