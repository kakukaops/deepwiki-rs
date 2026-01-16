# Phase 1: Project Discovery

**Objective**: Identify project structure, language, and key entry points.

## Step 1: Scan Directory Structure
Execute the following to get a high-level overview:
```bash
# Get file count to determine scale
find . -type f | wc -l

# Visual overview (limit depth to avoid context overflow)
tree -L 3 -I 'node_modules|target|build|dist|vendor|.git|.idea'
```

## Step 2: Identify Languages & Stack

Look for configuration files to determine the tech stack. Use find or ls patterns:

- **Python**: requirements.txt, pyproject.toml, setup.py
    
- **JavaScript/TS**: package.json, tsconfig.json
    
- **Java**: pom.xml, build.gradle
    
- **Go**: go.mod
    
- **Rust**: Cargo.toml
    
- **C/C++**: CMakeLists.txt, Makefile
    

## Step 3: Locate Entry Points

Identify the main entry points of the application (e.g., main.py, index.js, Application.java).

**Output Requirement**:  
Before moving to Phase 2, summarize:

1. Primary Language
    
2. Build System
    
3. Project Scale (Small/Medium/Large)
    
4. Key Entry Point Paths

## Step 4: Context Usage Report

Before proceeding, estimate the context used by the file lists.
```bash
# Estimate token count of the tree output (approx 4 chars = 1 token)
tree -L 2 -I 'node_modules|target|build|dist|vendor|.git' | wc -c
```
**Action**: Report "Context Stats: [Bytes] bytes (~[Bytes/4] tokens)" in your summary.

**Output Requirement**:  
Summarize:

1. Primary Language
    
2. Build System
    
3. Project Scale (Small/Medium/Large)
    
4. Key Entry Point Paths

---