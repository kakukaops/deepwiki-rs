# Execution Model

The skill operates as a deterministic pipeline.

Execution flow:

1. Load core role and principles
2. Execute Phase 1: Discovery
3. Detect primary and secondary languages
4. Load applicable language addendum plugins
5. Execute Phase 2 with plugin enrichment
6. Execute Phase 3 using templates
7. Execute Phase 4 diagram generation
8. Execute Phase 5 quality review
9. Present summary report

At no point should the agent skip phases.
