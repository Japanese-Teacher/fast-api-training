from unittest.mock import Mock

from app.services.book_service import BookService, get_book_service


def test_happy_path():
    mock = Mock()
    mock.get_books = Mock(return_value=1)
    book_service = BookService(
        book_repository=mock
    )
    assert book_service.get_books() == 1
