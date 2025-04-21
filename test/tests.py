from http import client


def test_foo() -> None:
    assert True


def test_add_book_success() -> None:
    status_code_success = 200
    new_book = {"id": 3, "title": "New Book", "author": "New Author"}
    response = client.post("/books", json=new_book)
    assert response.status_code == status_code_success
    assert response.json()["title"] == "New Book"