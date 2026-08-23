# Python Environment & Package Management Setup

A professional Python workspace setup demonstrating virtual environments, package management best practices, and lockfile compilation.

## 🛠 Skills & Tools Applied
* **Command Line (PowerShell):** Directory navigation and environment controls.
* **Virtual Environments (`venv`):** Isolated dependency management.
* **Package Management (`pip` & `pip-tools`):** Managing dependencies with `requirements.in` and compiling locked `requirements.txt`.
* **Project Structuring:** Professional layout (`src/`, `tests/`, `.gitignore`).

## 📁 Project Directory Layout
```text
day20_integration/
│
├── src/                  # Core application source code
│   └── app.py
├── tests/                # Test suite directory
├── .gitignore            # Excludes env/ and temporary files
├── requirements.in       # High-level direct dependencies
└── requirements.txt      # Locked dependency versions
