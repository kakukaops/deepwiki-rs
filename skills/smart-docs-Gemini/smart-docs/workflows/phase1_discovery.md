# Phase 1: Project Discovery

**Objective**: Identify project structure, language, and key entry points.

## Step 0: Context Safety Check
Before listing files, check the scale of the repository:
```bash
# Check total file count
find . -type f -not -path '*/.*' | wc -l
```
Decision: If file count > 1000, do NOT use recursive tree without depth limits.

## Step 1: Scan Directory Structure

Use a hybrid approach to see deep structure without token explosion:

1. **Overview (Files & Dirs)**: See immediate root context.
    ```bash
    tree -L 2 -I 'node_modules|target|build|dist|vendor|.git|.idea'
    ```
    
2. **Deep Skeleton (Directories Only)**: See the full architectural shape up to 6 levels deep.
    ```bash
    # -d: list directories only (very token cheap)
    tree -d -L 7 -I 'node_modules|target|build|dist|vendor|.git|.idea'
    ```

**Context Check**: Estimate tokens used by these tree outputs (Chars / 4).
  
    
## Step 2: Identify Languages & Stack

Look for configuration files. Use find to locate them regardless of depth:
```bash
find . -maxdepth 7 -name "package.json" -o -name "pom.xml" -o -name "go.mod" -o -name "Cargo.toml" -o -name "requirements.txt" -o -name "CMakeLists.txt"
```

**Context Check**: Estimate tokens used by these tree outputs (Chars / 4).


## Step 3: Locate Entry Points

**Do NOT rely on the tree output.** Use find to locate potential entry points deeply nested in the structure.

**Common Patterns**:
```bash
find src -name "main.py" -o -name "index.js" -o -name "Application.java" -o -name "main.go" -o -name "main.rs" -o -name "main.cpp"
```

**Context Check**: Estimate tokens used by these tree outputs (Chars / 4).


## Step 4: Context Usage Report

Before proceeding, estimate the context used.  
**Action**: Report "Context Stats: [Bytes] bytes (~[Bytes/4] tokens)" in your summary.

**Output Requirement**:  
Summarize:

1. Primary Language
    
2. Build System
    
3. Project Scale (Small/Medium/Large)
    
4. Key Entry Point Paths (Full paths found via find)

---