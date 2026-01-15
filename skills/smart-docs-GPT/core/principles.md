# Core Principles

1. Progressive Analysis  
   Analyze incrementally; never attempt to read the entire codebase blindly.

2. Architecture First  
   Focus on system structure, responsibilities, and boundaries before implementation details.

3. C4 Model Alignment  
   Use C4 levels (Context, Container, Component) as the primary documentation lens.

4. Explicit Artifacts  
   Every phase must produce explicit artifacts.

5. Templates Over Freeform  
   Prefer structured templates over ad-hoc writing.

6. Language Awareness via Plugins  
   Language-specific knowledge must come from plugins, not assumptions.

7. Source-of-Truth First
   Architectural inference MUST prioritize the primary source of truth for the language or ecosystem
   (e.g., build systems for C/C++, runtime frameworks for web apps)

