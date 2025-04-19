mypy:
  mypy main.py

ruff:
  ruff check

lint: mypy ruff