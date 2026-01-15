# Rust Language Addendum

---

## Identification Rules

- Cargo.toml
- Cargo.lock
- src/main.rs
- src/lib.rs

---

## Structural Units

- Crate (package)
- Module (mod)
- Trait
- Binary vs Library targets

---

## Architecture Signals

- Cargo workspace members indicate subsystem boundaries
- Traits used as abstraction layers
- Async runtimes (tokio, async-std) indicate concurrency model
- Error handling via Result / thiserror / anyhow

---

## Documentation Focus

- Ownership and borrowing semantics
- Trait-based polymorphism
- Error propagation paths
- Async execution model

---

## Diagram Preferences

- Module dependency graph
- Trait implementation relationships
- Async call flow (sequence diagrams)
