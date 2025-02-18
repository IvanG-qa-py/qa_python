import pytest
from main import BooksCollector


@pytest.fixture
def book_collection():
    book_collection = BooksCollector()
    return book_collection
