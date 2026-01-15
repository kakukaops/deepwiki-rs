# Language Plugin Base Contract

This document defines the mandatory contract for all language plugins.

A language plugin augments (but never overrides) the core documentation pipeline.

---

## 1. Identification Rules

The plugin MUST define:
- File patterns used to detect the language
- Build / dependency descriptors
- Entry-point conventions

The plugin MUST NOT assume the language is present unless detection evidence exists.

---

## 2. Structural Units

The plugin MUST define:
- What constitutes a “module”
- What constitutes a “component”
- Typical directory or namespace boundaries

These definitions are used during Phase 2 (Architecture Analysis).

---

## 3. Architecture Signals

The plugin SHOULD define:
- Common architectural patterns in this ecosystem
- Signals indicating layering or boundaries
- Framework-specific conventions (if applicable)

All signals must be evidence-based.

---

## 4. Documentation Focus

The plugin MUST define:
- What concepts deserve emphasis
- What concepts are typically boilerplate and can be de-emphasized

This influences Deep Dive content generation.

---

## 5. Diagram Preferences

The plugin SHOULD recommend:
- Preferred diagram types
- Diagrams that best express intent in this language ecosystem

---

## Safety Rules

A language plugin MUST NOT:
- Reorder pipeline phases
- Remove mandatory documentation artifacts
- Invent features not observed in the codebase
