# Strategy: Go

## Configuration
- **Extensions**: `.go`
- **Manifest Files**: `go.mod`
- **Ignore Paths**: `vendor`, `bin`

## Analysis Heuristics
1.  **Module Definition**: Go Modules, package directories.
2.  **Interface**: `interface` types, Struct composition.
3.  **Key Patterns**: Goroutines, Channels, `defer`, Error handling (`if err != nil`).