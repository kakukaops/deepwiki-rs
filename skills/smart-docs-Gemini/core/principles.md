# Operating Principles

1.  **Dynamic Strategy Loading**: Never assume a generic approach. Always detect the language stack first, then load the corresponding `languages/*.addendum.md` strategy.
2.  **Progressive Disclosure**: Start from the file system root (Context), zoom into packages (Container), and finally dissect files (Component). Do not read all files at once.
3.  **Visual First**: Complex logic must be explained via Mermaid diagrams (C4, Sequence, Class), not just text.
4.  **C4 Model Compliance**: All architecture documents must map to Context, Container, or Component levels.
5.  **Markdown Purity**: Output valid, well-structured Markdown that renders correctly in standard viewers.