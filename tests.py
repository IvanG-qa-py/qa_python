from main import BooksCollector
import pytest
from qa_python.conftest import books_collection


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Успех или успеть',
                                      'Преступление и наказание',
                                      'Граф Монте-Кристо'
                                      ])
    def test_add_new_book_name_is_positive(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()


    def test_add_new_book_added_book_twice_is_negative(self):
        book_collector = BooksCollector()
        book_collector.add_new_book('Война и Мир')
        book_collector.add_new_book('Война и Мир')
        assert book_collector.get_books_genre() == {'Война и Мир': ''}


    @pytest.mark.parametrize('book', ['',
                                      'Невероятное пари, или Истинное происшествие, благополучно завершившееся сто лет назад'])
    def test_add_new_book_more_negative_sizes(self, book):
        book_collector = BooksCollector()
        assert not book_collector.add_new_book(book)


    def test_set_book_genre_valid_name(self):
        book_collector = BooksCollector()
        book_collector.add_new_book('Дюна')
        book_collector.set_book_genre('Дюна', 'Фантастика')
        assert book_collector.get_books_genre() == {'Дюна': 'Фантастика'}


    @pytest.mark.parametrize('name, genre',
                             [('Лес', 'Ужасы'),
                              ('12 стульев', 'Комедии')
                              ])
    def test_get_book_genre_by_name(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_book_genre(name) == genre


    @pytest.mark.parametrize('name, genre',
                             [('Лес', 'Ужасы'),
                              ('12 стульев', 'Комедии')
                           ])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        book_collector = BooksCollector()
        book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.get_books_with_specific_genre(genre) == [name]


    def test_get_books_for_children(self, books_collection):
        my_collection = books_collection
        books = ['Симбиоз', 'Демон', 'Внутри убийцы', 'Гадкий Я', 'Ревизор']
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        for i in range(5):
            my_collection.add_new_book(books[i])
        for i in range(5):
            my_collection.set_book_genre(books[i], genre[i])
        assert len(
            my_collection.get_books_for_children()) == 3 and books_collection.get_books_for_children() == [
                   'Симбиоз', 'Гадкий Я', 'Ревизор']


    def test_add_book_in_favorites_positive_case(self):
        book_collector = BooksCollector()
        book_collector.add_new_book('Гарри Поттер и Кубок огня')
        book_collector.add_book_in_favorites('Гарри Поттер и Кубок огня')
        assert 'Гарри Поттер и Кубок огня' in book_collector.favorites


    def test_delete_book_from_favorites_positive_case(self):
        book_collector = BooksCollector()
        book_collector.add_new_book('Алиса в Стране чудес')
        book_collector.add_book_in_favorites('Алиса в Стране чудес')
        book_collector.delete_book_from_favorites('Алиса в Стране чудес')
        assert 'Алиса в Стране чудес' not in book_collector.favorites


    @pytest.mark.parametrize('name', ['Успех или успеть',
                                      'Преступление и наказание',
                                      'Граф Монте-Кристо'
                                      ])
    def test_get_list_of_favorites_books_positive_case(self, name, books_collection):
        books_collection.add_new_book(name)
        books_collection.add_book_in_favorites(name)
        assert books_collection.get_list_of_favorites_books()