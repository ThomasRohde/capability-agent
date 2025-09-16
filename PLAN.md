# Implementation Plan

## Objective
Address the critical restart persistence bug and ensure OpenAI full logging captures response bodies as expected.

## Tasks
1. **Fix restart mode persistence bug**  
   - Update the save_leaf_progress workflow so progress snapshots include newly generated children when a leaf completes.  
   - Add regression coverage (unit or integration) verifying restart mode preserves generated nodes after an interruption.

2. **Capture response bodies in full logging mode**  
   - Defer response logging until LoggingResponse has read the body, or hook into the read path to emit the payload.  
   - Add a unit test covering the full log level with OPENAI_LOG_BODY enabled to ensure bodies are written.

3. **Retest CLI flows**  
   - Run existing automated tests.  
   - Perform a manual smoke test of cli.run with --restart and logging flags to confirm both fixes work together.

## Risks & Mitigations
- **Concurrency interactions in restart mode**: ensure thread-safe updates during progress saving; consider using per-leaf child aggregation or lock.  
- **Logging performance impact**: guard body logging to avoid large memory usage; stream or size-limit as needed.

## Deliverables
- Code changes with accompanying tests.  
- Updated documentation or changelog entries if required.
