# Phase 2: Architecture Analysis

## Purpose

Infer system architecture, boundaries, and design intent.

Language-Specific Guidance:
For build-driven ecosystems (e.g., C/C++),
architecture SHOULD be derived primarily from
build targets, link dependencies, and artifact boundaries,
and NOT from directory layout or namespace structure alone.

This phase answers:
- How is the system structured?
- What are the major components?
- How do components interact?

---

## Mandatory Actions

1. Module Identification
   - Identify top-level modules/packages
   - Map directories to responsibilities

2. Dependency Mapping
   - Inspect imports / use / require statements
   - Distinguish internal vs external dependencies

3. Boundary Detection
   - API vs domain vs infrastructure
   - UI vs backend vs data

4. Pattern Recognition
   - Layered architecture
   - MVC / Hexagonal / Clean
   - Event-driven
   - Microservice vs monolith

---

## Plugin Interaction

Language plugins MAY:
- Redefine what a “module” means
- Provide framework-specific heuristics
- Highlight idiomatic patterns

Language plugins MUST NOT:
- Introduce assumptions without evidence

---

## Output Artifacts

You MUST produce:

### architecture.modules
- List of modules
- Responsibility per module
- Key files per module

### architecture.patterns
- Detected patterns
- Evidence supporting each pattern
