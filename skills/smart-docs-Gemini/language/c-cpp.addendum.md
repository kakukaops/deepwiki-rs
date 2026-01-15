# Strategy: C/C++

## Configuration
- **Extensions**: `.c`, `.cpp`, `.h`, `.hpp`, `.cc`, `.cxx`
- **Manifest Files**: `CMakeLists.txt`, `Makefile`, `configure.ac`, `conanfile.*`
- **Ignore Paths**: `build`, `cmake-build-*`, `bin`, `obj`, `lib`, `.deps`

## Analysis Heuristics
1.  **Module Definition**: Defined by build targets (`add_library`, `add_executable`).
2.  **Interface vs Impl**: Strictly separate `.h` (Interface) from `.cpp` (Implementation).
3.  **Key Patterns**: RAII (Resource Acquisition Is Initialization), Pimpl Idiom, Smart Pointers (`std::unique_ptr`), Macros.