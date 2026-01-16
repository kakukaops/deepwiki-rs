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
   *Decision*: If a file is > 100KB, rely **strictly** on `analyze_code.py` output. Do NOT read the file content directly.

## Step 1: Structural Extraction (The "Eye")
Run the analysis tool for key files identified in Phase 1:
```bash
python3 tools/analyze_code.py <file_path>
```
**Target Discovery (Essential for Deep/Large Repos)**:  
Since Phase 1 only showed directory skeletons, use find to locate source files in specific modules before analyzing.

```bash
# Example: Find top 10 java files in a specific deep module
find src/main/java/com/core/service -maxdepth 1 -name "*.java" | head -n 10
```

**Large Repo Strategy**:

- **Breadth-First**: Pick 1-2 representative files per folder.
    
- **Focus**: "God Files" and Interfaces.
    
- **Recursive Summarization**: Analyze -> Summarize -> **Discard JSON** -> Next.

 **Context Check**: After each file analysis, estimate the size of the JSON output. If > 2000 chars (~500 tokens), consider summarizing and clearing it immediately.



## Step 2: Conceptual Mapping (The "Brain") - **CRITICAL STEP**

After receiving the JSON structure, perform **Concept Clustering**:

1. **Identify Core Concepts**: (God Classes, Interfaces) -> core-concepts/
    
2. **Identify Data Structures**: (DTOs, Models) -> data-structures/
    
3. **Identify Pipelines**: (Sequential calls) -> pipelines/
    
4. **Group by Intent**: (e.g., "Networking Layer")
    

> **Context Check**: Report current context load before generating the final map.

**Output Requirement**:  
Output a **Concept Map** (Core Concepts, Data Models, Functional Areas) to guide Phase 3.

---
