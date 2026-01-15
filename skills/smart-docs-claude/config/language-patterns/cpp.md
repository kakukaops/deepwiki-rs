# C/C++ Language Analysis Patterns

This file defines how to analyze C/C++ projects.

## File Extensions

### Source Files
- `.c` - C source files
- `.cpp` - C++ source files
- `.cc` - C++ source files (Google style)
- `.cxx` - C++ source files (alternative)
- `.c++` - C++ source files (rare)

### Header Files
- `.h` - C/C++ header files
- `.hpp` - C++ header files
- `.hh` - C++ header files (alternative)
- `.hxx` - C++ header files (alternative)
- `.h++` - C++ header files (rare)

**Note**: All extensions should be recognized equally.

---

## Build System Detection

### Priority Order
1. CMake
2. Meson
3. Ninja
4. Autotools
5. Make (plain)

### Detection Commands

```bash
# Find build system files
find . -name "CMakeLists.txt" 2>/dev/null                    # CMake
find . -name "meson.build" 2>/dev/null                       # Meson
find . -name "build.ninja" 2>/dev/null                       # Ninja
find . -name "configure.ac" -o -name "configure.in" 2>/dev/null  # Autotools
find . -name "Makefile" -o -name "*.mk" 2>/dev/null         # Make
```

### Build System Characteristics

**CMake**:
- Modern, cross-platform
- Common in open-source projects
- Dependencies: `conanfile.txt`, `conanfile.py`, `vcpkg.json`

**Meson**:
- Modern, fast build system
- Python-based configuration
- Used by GNOME, systemd

**Autotools**:
- Traditional Unix build system
- `configure.ac`, `Makefile.am`
- Generate with autoconf/automake

**Make**:
- Simple, universal
- Direct Makefile
- May be hand-written or generated

---

## Module Discovery

### Directory Structure Patterns

```
Typical C/C++ Project:
├── include/          # Public headers (API)
│   └── mylib/
│       ├── public_api.h
│       └── types.h
├── src/              # Implementation
│   ├── core/
│   │   ├── engine.cpp
│   │   └── private.h
│   └── utils/
│       └── helpers.cpp
├── lib/              # Compiled libraries
├── test/             # Tests
└── CMakeLists.txt
```

### Module Identification

**By Directory**:
- Each subdirectory in `src/` typically represents a module
- `include/` contains public API headers
- Private headers usually in `src/` alongside implementation

**By Namespace**:
```cpp
namespace mylib {
namespace core {
    // Core functionality
}
namespace utils {
    // Utilities
}
}
```

**By CMake Targets**:
```cmake
add_library(mylib_core ...)
add_library(mylib_utils ...)
```

### Discovery Strategy

1. **Scan directory structure**: `src/`, `include/`, `lib/`, `modules/`
2. **Use unlimited depth Glob**: `**/*.{cpp,cc,cxx,c++,h,hpp,hh,hxx,h++}`
3. **Group by parent directory**: Organize files by containing folder
4. **Identify module boundaries**: Based on directories, namespaces, or CMake targets

---

## Code Analysis Patterns

### Functions

**Function Declarations** (in headers):
```cpp
// Regular function
ReturnType functionName(Type1 param1, Type2 param2);

// Member function
class MyClass {
public:
    ReturnType methodName(Type param);
};

// Template function
template<typename T>
T processData(T input);
```

**Extraction Command**:
```bash
# Find function declarations in headers
grep -rn "^\s*\(virtual\|static\|inline\)*\s*\w\+\s\+\w\+\s*(" include/ src/ 2>/dev/null | grep -v "^\s*//"

# Find class member functions
grep -rn "^\s*\w\+\s\+\w\+::\w\+\s*(" src/ 2>/dev/null
```

### Classes and Structs

**Class Definitions**:
```cpp
class MyClass {
private:
    int privateData;
protected:
    void protectedMethod();
public:
    MyClass();
    void publicMethod();
};

struct MyStruct {
    int field1;
    double field2;
};
```

**Extraction Command**:
```bash
# Find class definitions
grep -rn "^class\s\+\w\+" include/ src/ 2>/dev/null

# Find struct definitions
grep -rn "^struct\s\+\w\+" include/ src/ 2>/dev/null
```

### Templates

**Template Patterns**:
```cpp
// Function template
template<typename T>
T max(T a, T b);

// Class template
template<typename T>
class Container {
    T data;
};

// Template specialization
template<>
class Container<int> {
    // Specialized for int
};
```

**Documentation Focus**:
- Template parameters and constraints
- Specializations
- SFINAE patterns
- Concepts (C++20)

### Macros

**Preprocessor Macros**:
```cpp
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define API_EXPORT __declspec(dllexport)
```

**Extraction Command**:
```bash
# Find macro definitions
grep -rn "^#define\s\+\w\+" include/ src/ 2>/dev/null
```

### Namespaces

**Namespace Patterns**:
```cpp
namespace company {
namespace project {
namespace module {
    // Code here
}
}
}

// C++17 nested namespace
namespace company::project::module {
    // Code here
}
```

**Extraction Command**:
```bash
# Find namespace declarations
grep -rn "^namespace\s\+\w\+" include/ src/ 2>/dev/null
```

---

## API Documentation Extraction

### Public API Identification

**Headers in `include/` directory**:
```bash
# Find all public headers
find include/ -name "*.h" -o -name "*.hpp" -o -name "*.hh" 2>/dev/null
```

**Public vs Private**:
- `include/` → Public API (for library users)
- `src/` → Private implementation
- `src/*.h` → Private headers (not for users)

### Documentation Comments

**Doxygen Style**:
```cpp
/**
 * @brief Processes input data
 * @param input The input data to process
 * @return Processed result
 * @throws std::runtime_error if processing fails
 */
ReturnType processData(InputType input);
```

**Extraction Command**:
```bash
# Find Doxygen comments
grep -rn "/\*\*" include/ src/ 2>/dev/null
```

---

## Complexity Indicators

### Lines of Code per Function

```bash
# Count lines between function definition and closing brace
# This is a heuristic - actual implementation may vary
```

### Cyclomatic Complexity

Count decision points:
- `if`, `else if`, `else`
- `for`, `while`, `do-while`
- `switch`, `case`
- `&&`, `||` in conditions
- `? :` ternary operator
- `catch` blocks

```bash
# Simple heuristic: count control flow keywords
grep -c "\(if\|for\|while\|switch\|case\|catch\)" file.cpp
```

### Nesting Depth

```bash
# Count maximum indentation level
# Heuristic: count leading spaces/tabs
```

### Parameter Count

```bash
# Count parameters in function signature
# Functions with >5 parameters should be flagged
```

---

## Key Patterns to Document

### Memory Management

**RAII (Resource Acquisition Is Initialization)**:
```cpp
class FileHandle {
    FILE* file;
public:
    FileHandle(const char* name) : file(fopen(name, "r")) {}
    ~FileHandle() { if(file) fclose(file); }
};
```

**Smart Pointers**:
```cpp
std::unique_ptr<Type> ptr;
std::shared_ptr<Type> sharedPtr;
std::weak_ptr<Type> weakPtr;
```

### Header/Source Organization

**Header (.h)**:
- Class declarations
- Function declarations
- Inline functions
- Template definitions
- Constants and macros

**Source (.cpp)**:
- Function implementations
- Static variables
- Helper functions

### Include Guards

```cpp
// Traditional
#ifndef MYHEADER_H
#define MYHEADER_H
// ...
#endif

// Modern (C++11)
#pragma once
```

### Compilation Dependencies

**Forward Declarations** (reduce compilation dependencies):
```cpp
// In header
class MyClass;  // Forward declaration

void processClass(MyClass* obj);
```

### Platform-Specific Code

```cpp
#ifdef _WIN32
    // Windows-specific code
#elif defined(__linux__)
    // Linux-specific code
#elif defined(__APPLE__)
    // macOS-specific code
#endif
```

### Template Usage

**Document**:
- Template parameters
- Constraints (concepts in C++20)
- Common instantiations
- Specializations

---

## Build Artifacts to Ignore

When discovering files, exclude:

```
build/
cmake-build-*/
*.o
*.obj
*.a
*.so
*.dll
*.dylib
*.exe
.cache/
compile_commands.json
```

---

## Documentation Focus Areas

When documenting C/C++ code, emphasize:

1. **Memory Management**
   - Who owns what
   - RAII patterns
   - Smart pointer usage
   
2. **Header/Source Organization**
   - What goes in headers vs source
   - Include dependencies
   - Compilation units
   
3. **Build System**
   - How to build the project
   - Dependencies and their management
   - Build options and configurations
   
4. **Platform Support**
   - Target platforms
   - Platform-specific code sections
   - Conditional compilation
   
5. **Template Usage**
   - Template parameters
   - Instantiation examples
   - Specializations
   
6. **Public API**
   - Clear separation from implementation
   - API stability guarantees
   - Deprecated functions

---

## Example Analysis Output

```markdown
## C++ Project Analysis

**Build System**: CMake 3.20+
**Standard**: C++17
**Compiler Requirements**: GCC 9+, Clang 10+, MSVC 2019+

**Module Structure**:
- `core/` (15 files, 3200 LOC) - Core engine
- `utils/` (8 files, 1100 LOC) - Utility functions
- `api/` (5 files, 800 LOC) - Public API

**Public API**: 45 functions, 12 classes in `include/mylib/`

**Memory Management**: Modern C++ (smart pointers, RAII)

**Platform Support**: Windows, Linux, macOS

**Key Patterns**:
- Factory pattern for object creation
- RAII for resource management
- Template metaprogramming for compile-time optimization
```

---

*Use this information when executing Phase 2 (Architecture Analysis)*