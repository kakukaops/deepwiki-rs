# Phase 2: Structural Analysis

**Objective**: Use the `analyze_code.py` tool to extract precise metadata (AST) from source code.

**CRITICAL RULE**: Do NOT read source code files directly using the `Read` tool unless absolutely necessary for business logic understanding. Use the tool below to get structural data.

## Tool Usage
Run the analysis tool for each key file identified in Phase 1:

```bash
python3 tools/analyze_code.py <file_path>
```

**Example**:

```bash
python3 tools/analyze_code.py src/main.py
```

## Execution Strategy

1. **Core Modules First**: Analyze entry points and core domain logic files first.
    
2. **Batch Processing**: If the project is large, analyze files in batches of 5-10 to avoid output truncation.
    
3. **Ignore trivial files**: Do not analyze simple DTOs, generated code, or test files in this phase.
    

## Data Interpretation

The tool outputs JSON containing:

- **structure**: A list of defined symbols (Functions, Classes).
    
- **start_line / end_line**: Location of the code block.
    
- **complexity**: Cyclomatic complexity score (if available).
    

Use this JSON data to build a mental model of:

- **Class Hierarchy**: Who inherits from whom?
    
- **Public API**: What functions are exposed?
    
- **Code Health**: Which functions are too complex (>10 complexity)?
    

**Output Requirement**:  
Summarize the findings for each module:

- "Module X contains Class Y with methods [a, b, c]..."
    
- "Key algorithm is in function Z (complexity: 15)..."

---