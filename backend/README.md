## 💻 Run Locally

1. **Create a Virtual Environment**

```bash
python3 -m venv venv
```

2. **Activate the Virtual Environment**

```bash
source venv/bin/activate
```

3. **Install all the required packages**

```bash
pip install -r requirements.txt
```

4. **Execute the Script**

```bash
python3 main.py
```

5. **Run FastAPI using Uvicorn**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
