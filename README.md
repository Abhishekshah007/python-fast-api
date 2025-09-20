# Project Purpose

A minimal FastAPI service with a health check and CI that lints with Ruff and runs pytest on every push/PR to demonstrate a clean, reproducible backend setup.

## Requirements

- Python 3.8+  
- Git installed locally  
- Codespaces or a local venv for isolation

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run

Start the development server with Uvicorn and auto‑reload enabled:

```bash
uvicorn main:app --reload
```

- Open [127.0.0.1:8000](http://127.0.0.1:8000) for the root endpoint  
- Open [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive docs

## API Routes

- `GET /` — Returns `{"message": "Hello World"}` for a quick smoke test
- `GET /health` — Returns `{"status": "OK"}` as a simple health check

## Tests

Run the test suite from the repository root so imports resolve correctly:

```bash
python -m pytest -q
```

## Lint

Run Ruff to lint the codebase (configuration in `pyproject.toml`):

```bash
ruff check .
```

## Continuous Integration

GitHub Actions workflow at `.github/workflows/ci.yml` installs dependencies, runs Ruff, and executes pytest on push and pull_request to `main`.

## Optional: Codespaces

Use **Codespaces → Create codespace on main** to validate the app in a clean, cloud dev container. Forwarded ports expose the running Uvicorn server in the browser.