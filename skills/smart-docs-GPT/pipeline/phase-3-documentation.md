# Phase 3: Documentation Generation

## Purpose

Transform analysis artifacts into structured documentation.

This phase answers:
- How do we explain this system to humans?
- How do new contributors understand it?

---

## Mandatory Documents

The following documents MUST be generated:

1. Project Overview
2. Architecture Overview
3. Workflow Overview
4. Deep Dive documents (per major module)

---

## Template Rules

- Use templates from `/templates`
- All template variables MUST be populated
- Do not invent features not observed in analysis

---

## Scope Rules

- Focus on behavior and responsibility, not implementation trivia
- Avoid line-by-line explanations
- Prefer diagrams + narrative

---

## Output Artifacts

- `/docs/1. Project Overview.md`
- `/docs/2. Architecture Overview.md`
- `/docs/3. Workflow Overview.md`
- `/docs/4. Deep Dive/*.md`
