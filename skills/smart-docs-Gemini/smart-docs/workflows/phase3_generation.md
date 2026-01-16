# Phase 3: Documentation Generation (Concept-Oriented)

**Objective**: Synthesize the analysis data into a DeepWiki-style, concept-first documentation suite.

## Step 0: Context Budgeting
1. **Check Output Directory**: Ensure you are writing to `docs/` (standard directory).
2. **Budget**: If conversation history is too long, focus on generating one section at a time.

## Documentation Strategy
Do NOT just mirror the file system. Organize by **Value** and **Concept**.

## Document Types & Templates
- **Core Concepts**: `templates/core_concept.md`
- **Data Structures**: `templates/data_structures.md`
- **Architecture**: `templates/architecture_code.md`
- **API Reference**: `templates/module_api.md`

## Output Action
Use the `Write` tool to save files to the `./docs/` directory structure.

**Execution Loop**:
For each document you generate:
1. Write the content.
2. Verify written size:
```bash
ls -lh docs/<filename>
```
1. **Context Check**: "Generated [File] (~[Bytes] bytes). Context Load: [Status]."
    

Target Structure:

- docs/index.md   
- docs/core-concepts/... 
- docs/data-structures/... 
- docs/pipelines/...  
- docs/api-reference/...  
- docs/reference/...