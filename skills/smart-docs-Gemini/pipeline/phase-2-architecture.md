# Phase 2: Architecture Analysis

**Objective**: Map the software anatomy using the loaded Strategy.

**Steps**:
1.  **Module Boundary Detection**:
    - Use the `module_definition` rule from the active Addendum to find logical boundaries (e.g., CMake Targets vs Rust Crates).
2.  **Dependency Mapping**:
    - Parse manifest files defined in `manifest_files` of the Addendum.
    - Differentiate between **Internal Deps** (Monorepo libs) and **External Deps** (3rd party).
3.  **Interface Extraction**:
    - Prioritize reading files matching the `interface_files` pattern in the Addendum (e.g., `.h` for C++, `traits` for Rust).
4.  **Pattern Recognition**:
    - Identify patterns listed in the Addendum's `key_patterns` section (e.g., RAII, Dependency Injection).