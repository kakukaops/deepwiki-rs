# Phase 1: Discovery & Strategy Loading

**Objective**: Identify the tech stack and load the language-specific "Addendum".

**Steps**:
1.  **Fingerprinting**: Run `ls -F` to identify key config files (e.g., `Cargo.toml`, `CMakeLists.txt`, `pom.xml`).
2.  **Strategy Injection**: Based on the fingerprint:
    - If C/C++ detected -> Activate rules from `languages/cpp.addendum.md` (if exists, else generic)
    - If Rust detected -> Activate rules from `languages/rust.addendum.md`
    - (and so on for other languages in `languages/`)
    - If unknown -> Load `languages/_base.md`
3.  **Noise Filtering**: Construct a `tree` command. You MUST exclude directories defined in the active Addendum's `ignore_paths` list.
4.  **Volume Analysis**: Count Lines of Code (LOC) targeting only the extensions defined in the active Addendum.