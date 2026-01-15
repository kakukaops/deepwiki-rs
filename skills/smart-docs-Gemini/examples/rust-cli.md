# Example: Rust CLI Tool

## Scenario

User asks:
"Generate documentation for this Rust CLI project."

---

## Discovery Signals

- Cargo.toml detected
- src/main.rs present
- clap dependency found

---

## Language Plugin Activated

- rust.addendum.md

---

## Pipeline Highlights

### Phase 1
- Identify as single-binary CLI tool
- LOC < 5k, non-workspace

### Phase 2
- Command parsing as core component
- Business logic separated from CLI layer

### Phase 3 Focus

- Command structure
- Argument validation
- Execution flow per subcommand

---

## Diagram Strategy

- Component graph: CLI → Core Logic
- Sequence diagram: Command execution path

---

## Output Characteristics

- Emphasis on CLI usage
- Minimal infrastructure discussion
- Clear command examples
