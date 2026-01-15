# Phase 1: Project Discovery

## Precondition:
If a build system or orchestration file is present
(e.g., CMakeLists.txt, Makefile, BUILD.bazel),
it MUST be analyzed before drawing any conclusions
about project structure or architecture.

## Purpose

Establish a high-level understanding of the project without deep code reading.

Precondition:
If a build system or orchestration file is present
(e.g., CMakeLists.txt, Makefile, BUILD.bazel),
it MUST be analyzed before drawing any conclusions
about project structure or architecture.

This phase answers:
- What is this project?
- How big is it?
- What language(s) does it use?
- Where are the entry points?

---

## Mandatory Actions

1. Directory Structure Scan
   - Use tree (depth ≤ 3)
   - Exclude common noise directories:
     node_modules, target, build, dist, vendor, .git, __pycache__

2. Code Size Estimation
   - Prefer `cloc`
   - Fallback to `wc -l` with common extensions

3. Entry Point Identification
   - README files
   - Build / dependency descriptors
   - Main entry files (language-dependent)

4. Minimal Reading
   - README.md (if present)
   - Primary build file(s)
   - One main entry file

---

## Language-Agnostic Signals

- Repository intent (library / service / CLI / app)
- Monorepo vs single package
- Presence of tests
- Presence of documentation

---

## Output Artifacts

You MUST produce:

### discovery.summary

- Project name
- Inferred purpose
- Primary language(s)
- Build system
- Estimated size (LOC, modules)
- High-level directory breakdown

No architectural conclusions are allowed in this phase.
