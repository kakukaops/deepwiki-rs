# Phase 2: Structural & Conceptual Analysis

**Objective**: Use static analysis to extract code structure AND map it to high-level business concepts.

**CRITICAL RULE**: Do NOT read source code files directly unless necessary. Use the tool below to get structural data.

## Step 0: Context Safety & Strategy Check
1. **Check Scale**:
```bash
   find . -type f -name "*.*" -not -path '*/.*' | wc -l
```
2. **Select Strategy**:
    
    - **Small (< 50 files)**: Analyze all.
        
    - **Medium (50 - 500 files)**: Analyze core modules.
        
    - **Large (> 500 files)**: **SAMPLING MODE (Strict)**.

3. **Check File Size**:  
    Before analyzing any specific file, check its size.  
    Decision: If a file is > 100KB, rely **strictly** on analyze_code.py output. Do NOT read the file content directly.

## Step 1: Structural Extraction (The "Eye")
Run the analysis tool for key files identified in Phase 1:
```bash
python3 tools/analyze_code.py <file_path>
```

### 🔴 Large Repository Strategy (>500 files)

**Do NOT try to analyze every file.** You will run out of context and time.

**1. Breadth-First Discovery (Depth 1-2)**:

- Identify the top-level folders (e.g., src/core, src/utils, src/api).
    
- Pick **1-2 representative files** from each folder to understand the pattern.
    
- Example: In src/models, analyze one model to understand the DTO pattern, then assume others are similar.
    

**2. Focus on "God Files"**:

- Use cloc or ls -lS (sort by size) to find the largest/most complex files. These usually contain the core logic.
    
- Analyze these specific files in detail.
    

**3. Ignore Implementation Details**:

- **SKIP**: Tests (*test*, *spec*), Mocks, Migrations, UI Components (unless core), Generated Code.
    
- **FOCUS**: Interfaces, Abstract Classes, Controllers, Service Managers, Entry Points.
    

**4. Recursive Summarization**:

- Analyze a module -> Write a 3-sentence summary into your "Long-term Memory" (Scratchpad) -> **Discard** the detailed JSON -> Move to next module.

**Context Monitoring**:  
After running the tool, check the size of the output immediately (mentally estimate based on the text length returned).  
If the JSON output seems massive (>2000 lines), **STOP** and summarize it immediately, then clear it from context if your tool supports it, or note to be concise in the next steps.

**Execution Strategy**:

1. **Core Modules First**: Prioritize entry points (main, app) and core domain logic.
    
2. **Batch Processing**: **MANDATORY**. Analyze files in small batches (e.g., 5 files at a time).
    
    - After each batch, summarize the findings into your memory and **clear** the raw JSON output from context if possible/needed.
        

## Step 2: Conceptual Mapping (The "Brain") - **CRITICAL STEP**

After receiving the JSON structure, you must perform **Concept Clustering**. Do NOT just list files.

**1. Identify Core Concepts**:  
Look for "God Classes", key Interfaces, or central Traits.

- Hint: Classes with many methods, high usage, or names like Manager, Engine, System, Core.
    
- **Action**: Flag these as candidates for the core-concepts/ documentation section.
    

**2. Identify Data Structures**:  
Look for classes/structs that are primarily data holders (few methods, many fields).

- Hint: DTOs, Configs, Models, Types.
    
- **Action**: Flag these for the data-structures/ documentation section.
    

**3. Identify Pipelines & Flows**:  
Look for sequential calls or chain patterns in the calls data.

- Hint: init -> validate -> process -> save.
    
- **Action**: Note these sequences to generate pipelines/ documentation later.
    

**4. Group by Functional Area**:  
Do not group by folder name alone. Group by **Intent**.

- Example: src/http and src/grpc -> **"Networking Layer"**.
    

**Output Requirement**:  
Before moving to Phase 3, output a **Concept Map**:

- **Core Concepts**: [List of key classes/interfaces]
    
- **Data Models**: [List of key data structures]
    
- **Functional Areas**: [Area Name] -> [List of Modules]


## Step 3: Context Usage Report

> **Context Stats**: Analyzed [N] key files (Selected from [Total] files). Strategy: [Sampling/Full].