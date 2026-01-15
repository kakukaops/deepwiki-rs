# Language Plugin Compliance Checklist

This checklist is used to validate whether a language plugin
is safe, complete, and compatible with the smart-docs skill.

Each language plugin SHOULD be reviewed against this checklist
before being added or modified.

---

## 1. Identification

- [ ] File patterns clearly defined
- [ ] Build / dependency descriptors specified
- [ ] Entry-point conventions documented
- [ ] Detection rules do not assume presence without evidence

---

## 2. Structural Model

- [ ] Definition of “module” provided
- [ ] Definition of “component” provided
- [ ] Mapping between directory / namespace and responsibility explained
- [ ] Structural units align with language idioms

---

## 3. Architecture Awareness

- [ ] Common architectural patterns listed
- [ ] Framework-specific conventions (if any) documented
- [ ] Boundary and layering signals are evidence-based
- [ ] No speculative or assumed patterns

---

## 4. Documentation Guidance

- [ ] Clear guidance on what to emphasize
- [ ] Clear guidance on what can be de-emphasized
- [ ] Guidance aligns with real-world usage of the language
- [ ] Does not force boilerplate explanations

---

## 5. Diagram Guidance

- [ ] Preferred diagram types specified
- [ ] Diagram recommendations match language strengths
- [ ] Diagram complexity kept reasonable (≤ 12 nodes)

---

## 6. Pipeline Safety

- [ ] Plugin does NOT reorder pipeline phases
- [ ] Plugin does NOT remove mandatory artifacts
- [ ] Plugin does NOT override templates
- [ ] Plugin only augments analysis and generation

---

## 7. Maintainability

- [ ] Plugin is self-contained
- [ ] Plugin is readable without external context
- [ ] Plugin can evolve independently
- [ ] Plugin changes do not require core changes

---

## Compliance Result

- [ ] Approved
- [ ] Requires changes

Reviewer Notes:
