# Strategy: Python

## Configuration
- **Extensions**: `.py`
- **Manifest Files**: `pyproject.toml`, `setup.py`, `requirements.txt`
- **Ignore Paths**: `__pycache__`, `venv`, `.env`, `*.egg-info`

## Analysis Heuristics
1.  **Module Definition**: Packages defined by `__init__.py`.
2.  **Interface**: Abstract Base Classes (ABCs), Type Hints.
3.  **Key Patterns**: Decorators, Context Managers (`with`), Generators.