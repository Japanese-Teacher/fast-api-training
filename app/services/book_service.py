from app.models import books_db


class BookService:

    def delete_book(
        self,
        book_id: int,
    ) -> None:
        for idx, book in enumerate(books_db):
            if book.id == book_id:
                books_db.pop(idx)
                return
        raise ValueError('Книга не найдена')

