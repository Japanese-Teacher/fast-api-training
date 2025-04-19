mypy:
  mypy app

ruff:
  ruff check --fix

lint: mypy ruff

run:
  uvicorn app.main:app --reload

TESTS_DIR := "tests/"

test:
    pytest {{TESTS_DIR}}