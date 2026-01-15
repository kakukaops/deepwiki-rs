# Strategy: Rust

## Configuration
- **Extensions**: `.rs`
- **Manifest Files**: `Cargo.toml`
- **Ignore Paths**: `target`

## Analysis Heuristics
1.  **Module Definition**: Defined by `mod.rs` or `lib.rs` visibility rules (`pub mod`).
2.  **Interface**: Defined by `trait` definitions.
3.  **Key Patterns**: Ownership, Borrowing, `Result<T, E>` handling, Async (`Tokio`).