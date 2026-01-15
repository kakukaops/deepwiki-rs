# Phase 3: Documentation Generation

**Objective**: Synthesize the analysis data into structured Markdown documentation.

## Guidelines
1. **One Source of Truth**: Base your documentation primarily on the JSON data from Phase 2.
2. **Professional Tone**: Use clear, technical language.
3. **Cross-Linking**: Link between documents using relative paths (e.g., `[See API](../api/module.md)`).

## Document Types & Templates

### 1. API Reference
For each major module, create an API document.
- **Input**: `analyze_code.py` JSON output.
- **Template**: `templates/module_api.md`
- **Content**: List Classes, Methods, Parameters, and Return types.

### 2. Architecture Code Structure (C4 Level 4)
Create a document describing the code organization.
- **Input**: Aggregated structure from Phase 2.
- **Template**: `templates/architecture_code.md`
- **Content**: Explain how classes relate and interact.

### 3. Complexity Report
Create a code quality report.
- **Input**: `complexity` fields from JSON.
- **Content**: List functions with complexity > 10 and recommend refactoring.

## Output Action
Use the `Write` tool to save files to the `./docs/` directory.
- `docs/api-reference/...`
- `docs/architecture/...`
- `docs/reference/complexity.md`

---