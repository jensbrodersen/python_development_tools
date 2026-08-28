# Python Dev Utilities

A lightweight collection of helper scripts and utility functions designed to streamline Python development and assist with code cleanup.

## Features

- **`find_duplicated_functions.py`**: Scans a project directory to detect identical or near-identical function signatures/implementations.
- **`find_unused_functions.py`**: Analyzes Python files to identify functions that are defined but never called across your codebase.

*More utility tools will be added over time as needed.*

## Installation

Install directly from GitHub using `pip`:

```bash
pip install git+https://github.com/jensbrodersen/python_development_tools.git
```
## Usage
```python
from python_development_tools import find_duplicated_functions, find_unused_functions

# Scan a target directory for duplicate functions
duplicates = find_duplicated_functions("/path/to/your/project")
print(duplicates)

# Detect unused functions in your project
unused = find_unused_functions("/path/to/your/project")
print(unused)
```

## Quickstart (CLI)
```bash
python -m python_development_tools.find_duplicated_functions /path/to/project
python -m python_development_tools.find_unused_functions /path/to/project
```
