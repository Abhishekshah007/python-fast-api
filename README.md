## 1. Create Project and Virtual Environment

**macOS/Linux**
```
mkdir my-fastapi-app && cd my-fastapi-app
python3 -m venv .venv
```

**Windows (PowerShell)**
```powershell
mkdir my-fastapi-app; cd my-fastapi-app
py -m venv .venv
```

## 2. Activate the Virtual Environment

**macOS/Linux**
```
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

## 3. Upgrade pip and Install Dependencies

Install FastAPI and Uvicorn inside the activated venv. The `standard` extra adds useful dev dependencies.

```
python -m pip install --upgrade pip
pip install fastapi "uvicorn[standard]"
```

## 4. Quick Verify

Create `main.py` and run a dev server. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to confirm JSON output.

```python
# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

```
uvicorn main:app --reload
```

## 5. Common Maintenance

Freeze current packages so others can reproduce the environment.

```
pip freeze > requirements.txt
```

Recreate environment from `requirements.txt` on a new machine.

```
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Deactivate when finished to return to the global interpreter.

```
deactivate
```