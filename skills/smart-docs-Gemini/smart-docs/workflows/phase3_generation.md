# Phase 3: Documentation Generation (Concept-Oriented)

**Objective**: Synthesize the analysis data into a DeepWiki-style, concept-first documentation suite.

## Step 0: Context Budgeting & Path Safety
1. **Check Output Directory**: Ensure you are writing to `docs/` (standard directory).
   - ❌ NO: `.docs/`, `.doc/`, `doc/`
   - ✅ YES: `docs/`
2. **Budget**: If conversation history is too long, focus on generating one section at a time.

## Documentation Strategy
Do NOT just mirror the file system. Organize by **Value** and **Concept**.

## Document Types & Templates

### 1. Core Concepts (High Priority)
For each "Core Concept" identified in Phase 2:
- **Template**: `templates/core_concept.md`
- **Content**: Explain *what* it is, *why* it exists, and link to its API reference.

### 2. Data Structures & Configuration
- **Template**: `templates/data_structures.md`
- **Content**: Group all Configs, DTOs, and Enums here. Don't bury them in API docs.

### 3. Architecture & Flows
- **Template**: `templates/architecture_code.md`
- **Content**: Focus on **Pipelines** and **Interactions** (how concepts relate).

### 4. Full API Reference (Low Priority / Appendix)
- **Input**: `analyze_code.py` JSON output.
- **Template**: `templates/module_api.md`
- **Content**: The exhaustive list of classes/functions for reference.

## Output Action
Use the `Write` tool to save files to the `./docs/` directory structure.

**Step-by-Step Reporting**:
After writing each file, verify its size:
```bash
ls -lh docs/<file_name>
```
**Context Stats**: Generated [File]. Size: [Bytes].

Target Structure:
- `docs/index.md`
- `docs/core-concepts/...`
- `docs/data-structures/...`
- `docs/pipelines/...`
- `docs/api-reference/...`
- `docs/reference/...`