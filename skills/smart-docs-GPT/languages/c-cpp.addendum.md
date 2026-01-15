# Language Addendum: C / C++

## Scope

This addendum applies to projects primarily written in:

- C
- C++
- Mixed C/C++ codebases

Including but not limited to:

- System libraries
- Daemons and services
- Embedded software
- Toolchains and runtimes
- Performance-critical components

---

## Primary Signals

### File Patterns

- *.c, *.h
- *.cpp, *.cc, *.cxx
- *.hpp, *.hh

### Build System Signals (High Priority)

- CMakeLists.txt
- Makefile
- meson.build
- BUILD / BUILD.bazel
- configure.ac / autogen.sh

> Build system files are the **primary source of truth** for structure.

---

## Structural Model (Overrides Base Assumptions)

### What Is a “Module”

A module is typically one of:

- A build target (library or binary)
- A directory mapped to a target
- A logical library inferred from link boundaries

**NOT necessarily:**

- A namespace
- A class hierarchy
- A header file

---

### What Is a “Component”

A component is inferred from:

- Static or shared library boundaries
- Link-time dependencies
- Public header exposure

Header-only libraries MAY be components if reused.

---

## Architecture Discovery Strategy

### Priority Order

1. Build graph (targets and dependencies)
2. Binary vs library separation
3. Public vs private headers
4. Directory structure
5. Code-level abstractions (last)

> Never assume architectural intent purely from directory names.

---

## Common Architectural Patterns

- Layered libraries (core → util → app)
- Platform abstraction layers (PAL)
- Plugin architectures via dynamic linking
- Interface segregation via headers
- Compile-time polymorphism (templates)

---

## Documentation Emphasis

### Emphasize

- Build and dependency graph
- Binary vs library responsibilities
- Ownership of memory and resources
- Threading and concurrency model
- ABI / API stability boundaries

### De-emphasize

- File-by-file explanation
- Class-level inheritance trees (unless dominant)
- High-level “business flow” if absent

---

## Diagram Guidance

### Recommended Diagrams

- Component diagrams based on build targets
- Dependency graphs (libraries → binaries)
- Runtime interaction diagrams for daemons
- Memory ownership diagrams (when relevant)

### Avoid

- Over-detailed class diagrams
- Diagrams assuming managed runtime behavior

---

## Known Pitfalls

- Do not infer architecture from headers alone
- Do not assume a single entry point
- Do not assume modern CMake conventions
- Do not assume RAII correctness without evidence

---

## Summary Guidance

C/C++ documentation should reflect **physical reality**:
build artifacts, link boundaries, and runtime behavior
are more important than abstract code structure.
