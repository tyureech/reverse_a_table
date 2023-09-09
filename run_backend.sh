/bin/sh

sleep 2

python initial_db.py

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000