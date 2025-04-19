from http import client


def test_add_book_success():
    new_book = {"id": 3, "title": "New Book", "author": "New Author"}
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    assert response.json()["title"] == "New Book"