CFU — Python helper files

This repository contains a small Python helper script at `scripts/hello.py`.

Quick run (PowerShell)

1) Run using the system Python (if `python` is on PATH):

```powershell
python .\scripts\hello.py
python .\scripts\hello.py --name "Your Name"
```

2) Recommended: use the provided PowerShell runner which creates a virtual environment and runs the script:

```powershell
# From the repository root
.\run.ps1 -Name "Your Name"
```

3) Manually create and activate a venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python .\scripts\hello.py --name "Your Name"
```

If `python` is not found on Windows, either:
- Install Python from https://www.python.org/downloads/windows and check "Add Python to PATH" during install, or
- Disable the Microsoft Store Python app execution alias in Settings > Apps > App execution aliases.

Adding more Python files

- Put scripts into `scripts/` for small tools.
- For reusable modules, create a package directory (for example `cfu/`) and add an `__init__.py`.
- Add dependencies to `requirements.txt` and install them into the venv with `pip install -r requirements.txt`.

Questions? Tell me if you want me to:
- add a `pyproject.toml` and configure packaging, or
- convert `scripts/hello.py` into a package with unit tests.