# EPOCH Development Environment

**Date:** 13 November 2026
**Owner:** Adithya
**Operating system:** Windows
**Shell:** PowerShell

## Python Selection

Python 3.11 was selected from the installed interpreters.

The system default Python is 3.15.2, so EPOCH commands explicitly
use the project virtual environment.

## Virtual Environment

Location: `.venv`

Python executable: `.venv\Scripts\python.exe`

Creation command:

`py -3.11 -m venv .venv`

Pip upgrade command:

`.\.venv\Scripts\python.exe -m pip install --upgrade pip`

## Verification

The following checks were executed successfully:

- Python version reported Python 3.11.x.
- pip was available and upgraded inside the virtual environment.
- sys.executable pointed to `D:\EPOCH\.venv\Scripts\python.exe`.
- Git was available.
- The active development branch was `feature/adithya-integrity-engine`.

## Environment Status

**Python environment:** VERIFIED

**Dependency installation:** PENDING

**Editable package installation:** PENDING

**Automated tests:** NOT RUN

## Reproducibility

To recreate the environment:

`py -3.11 -m venv .venv`

`.\.venv\Scripts\python.exe -m pip install --upgrade pip`

Install project dependencies using the command documented in the
engine README after reviewing pyproject.toml.
