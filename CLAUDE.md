# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Python CLI tool called `business-capgen` (package name: `capability-agent`) that augments business capability models. It reads JSON arrays of capability nodes, uses Jinja2 templates to generate prompts for each leaf node, calls OpenAI's API to generate sub-capabilities, validates them with Pydantic, and outputs an augmented JSON array.

## Key Commands

### Installation
```bash
# Global install with pipx (recommended)
pipx install .

# Editable local development install
pip install -e .
```

### Running the CLI
```bash
business-capgen \
  --input examples/model.json \
  --template examples/prompt.j2 \
  --output out.json \
  --max-capabilities 5 \
  --tasks 4 \
  --override-system-message examples/system.txt \
  --context-level full_tree,parent,siblings \
  --log-prompts logs/
```

### Environment Setup
- **Required**: Set `OPENAI_API_KEY` environment variable for API access
- Python 3.10+ required

## Code Architecture

### Package Structure
- **src/capability_agent/**: Main package directory
  - **cli.py**: Entry point, command-line interface using Typer
  - **models.py**: Pydantic models (Capability, CapabilityList) with UUID validation
  - **service.py**: Core augmentation logic with concurrent LLM calls
  - **llm.py**: OpenAI API integration
  - **prompting.py**: Jinja2 template rendering and context building
  - **io_utils.py**: File I/O, context parsing, and utilities

### Key Architectural Patterns

1. **Data Model**: 
   - Uses Pydantic for strict validation of capability nodes
   - Each node must have UUID4 `id`, `name`, `description`, optional `parent`
   - Extra fields preserved through processing
   - Parent-child relationships validated for integrity

2. **Processing Flow**:
   - Load and validate input JSON → Find leaf nodes → Generate prompts per leaf → Call LLM concurrently → Assign UUIDs to new nodes → Validate and write output

3. **Concurrency**: 
   - Uses ThreadPoolExecutor for parallel LLM calls (configurable via `--tasks`)
   - Rich progress bars show real-time generation status

4. **Template Context**: 
   - Builds hierarchical context (full tree, parent, siblings) based on `--context-level`
   - Renders Jinja2 templates with structured capability context

5. **Error Handling**: 
   - CLI exits with code 1 on any validation or processing error
   - Clear error messages via Rich console output

### Dependencies
- **openai**: LLM API calls (currently configured for gpt-5-nano)
- **typer**: CLI framework
- **jinja2**: Template engine for prompts
- **rich**: Terminal UI and progress bars
- **pydantic**: Data validation

### Code Style
- Line length: 100 characters (configured in pyproject.toml)
- Python 3.10+ type hints used throughout
- Ruff linter configuration in pyproject.toml