# Language Detection Configuration

This file defines how to detect and identify programming languages in a codebase.

## Language Detection Rules

| Language | File Extensions | Config Files | Entry Points | Package Indicators |
|----------|----------------|--------------|--------------|-------------------|
| **C/C++** | `.c`, `.cpp`, `.cc`, `.cxx`, `.c++`, `.h`, `.hpp`, `.hh`, `.hxx`, `.h++` | `CMakeLists.txt`, `Makefile`, `*.mk`, `configure.ac`, `meson.build`, `build.ninja` | `main.c`, `main.cpp`, `main.cc`, `main.cxx` | `CMakeLists.txt`, `conanfile.txt`, `conanfile.py`, `vcpkg.json` |
| **Rust** | `.rs` | `Cargo.toml` | `main.rs`, `lib.rs` | `Cargo.toml` workspace |
| **Java** | `.java` | `pom.xml`, `build.gradle`, `build.xml` | `Main.java`, `Application.java` | `pom.xml`, `build.gradle` |
| **Go** | `.go` | `go.mod`, `go.sum` | `main.go` | `go.mod` |
| **JavaScript** | `.js`, `.jsx` | `package.json` | `index.js`, `app.js`, `server.js` | `package.json` |
| **TypeScript** | `.ts`, `.tsx` | `tsconfig.json`, `package.json` | `index.ts`, `main.ts`, `app.ts` | `tsconfig.json` |
| **Python** | `.py` | `setup.py`, `pyproject.toml`, `requirements.txt` | `main.py`, `app.py`, `__main__.py` | `setup.py`, `pyproject.toml` |
| **PHP** | `.php` | `composer.json` | `index.php`, `app.php` | `composer.json` |

## Detection Algorithm

### Step 1: Count Files by Extension

```bash
# Count source files for each language
find . -type f -name "*.c" -o -name "*.cpp" -o -name "*.cc" -o -name "*.cxx" 2>/dev/null | wc -l  # C/C++
find . -type f -name "*.rs" 2>/dev/null | wc -l                                                    # Rust
find . -type f -name "*.java" 2>/dev/null | wc -l                                                  # Java
find . -type f -name "*.go" 2>/dev/null | wc -l                                                    # Go
find . -type f -name "*.js" -o -name "*.jsx" 2>/dev/null | wc -l                                  # JavaScript
find . -type f -name "*.ts" -o -name "*.tsx" 2>/dev/null | wc -l                                  # TypeScript
find . -type f -name "*.py" 2>/dev/null | wc -l                                                    # Python
find . -type f -name "*.php" 2>/dev/null | wc -l                                                   # PHP
```

### Step 2: Identify Config Files

```bash
# Use Glob to find configuration files (works at any depth)
# C/C++
find . -name "CMakeLists.txt" -o -name "Makefile" -o -name "meson.build" 2>/dev/null

# Rust
find . -name "Cargo.toml" 2>/dev/null

# Java
find . -name "pom.xml" -o -name "build.gradle" 2>/dev/null

# Go
find . -name "go.mod" 2>/dev/null

# JavaScript/TypeScript
find . -name "package.json" -o -name "tsconfig.json" 2>/dev/null

# Python
find . -name "setup.py" -o -name "pyproject.toml" -o -name "requirements.txt" 2>/dev/null

# PHP
find . -name "composer.json" 2>/dev/null
```

### Step 3: Determine Primary Language(s)

**Rules**:
1. If config file exists → High confidence for that language
2. Count source files → Language with most files is primary
3. Multiple languages → List all with >10% of total files
4. TypeScript + JavaScript → Report as TypeScript (superset)

**Example Logic**:
```
Total files: 500
- C++ files: 350 (70%)    → Primary language
- Python files: 100 (20%) → Secondary language
- Shell files: 50 (10%)   → Utility scripts (don't report)

Result: Primary: C++, Secondary: Python
```

## Language-Specific Pattern Files

After detecting language(s), read the corresponding pattern file(s):

- **C/C++** → Read `config/language-patterns/cpp.md`
- **Rust** → Read `config/language-patterns/rust.md`
- **Python** → Read `config/language-patterns/python.md`
- **Java** → Read `config/language-patterns/java.md`
- **Go** → Read `config/language-patterns/go.md`
- **JavaScript/TypeScript** → Read `config/language-patterns/javascript.md`
- **PHP** → Read `config/language-patterns/php.md`

## Multi-Language Projects

For projects with multiple languages:

1. **Identify all languages** with >5% of total files
2. **Read pattern files** for each identified language
3. **Document separately** in architecture overview
4. **Note integration points** between languages

### Common Multi-Language Patterns

- **Web Application**: TypeScript (frontend) + Python/Go/Java (backend)
- **System + Scripting**: C++ (core) + Python (tools/tests)
- **Native + Web**: Java/Swift (mobile) + JavaScript (web)
- **Data Pipeline**: Python (processing) + SQL (database)

## Architecture Type Detection

Based on files and structure:

| Pattern | Architecture Type |
|---------|------------------|
| `main.{c,cpp,rs,go}` | CLI Application |
| `server.js`, `app.py`, REST routes | Web Service/API |
| `include/` with public headers | Library |
| `*.a`, `*.so`, `*.dll` build targets | Shared Library |
| `package.json` with React/Vue/Angular | Frontend Application |
| `.ino` files, embedded keywords | Embedded System |
| Docker files, K8s configs | Containerized Service |

## Usage Example

```markdown
## Language Detection Results

**Primary Language**: C++ (70% of codebase)
- 350 `.cpp` and `.h` files
- Build System: CMake
- Architecture: Static Library

**Secondary Language**: Python (20% of codebase)
- 100 `.py` files
- Purpose: Testing and build tools
- Framework: pytest

**Next Step**: Read the following pattern files:
1. .claude/skills/smart-docs/config/language-patterns/cpp.md
2. .claude/skills/smart-docs/config/language-patterns/python.md
```

---

*After language detection, proceed to read the appropriate language pattern files*