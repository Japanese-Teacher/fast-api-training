mypy:
  mypy main.py

ruff:
  ruff check

lint: mypy ruff

run:
  uvicorn app.main:app --reload
