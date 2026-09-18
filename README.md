# Python App Template

A simple starter app in Python.

## Setup (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the app

```powershell
python -m app_template --name "World"
```

## Check your code

```powershell
ruff check .
mypy src
pytest
```
