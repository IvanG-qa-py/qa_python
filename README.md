## Unit tests for class BookCollector
---

### Fixture book_collection возвращает объект класса Bookcollector
---
### Реализованы следующие тестовые сценарии:

1. test_add_new_book_name_is_positive - проверка добавления книг
2. test_add_new_book_added_book_twice_is_negative - негативная проверка повторного добавления
3. test_add_new_book_negative_sizes - негативная проверка на невалидное название
4. test_set_book_genre_valid_name - проверка на добавление жанра
5. test_get_book_genre_by_name - проверка на вывод жанра по имени
6. test_get_books_with_specific_genre_by_genre - проверка вывода книги по жанру
7. test_get_books_for_children - проверка на вывод детского жанра
8. test_add_book_in_favorites_positive_case - проверка на добавление в избранное
9. test_delete_book_from_favorites_positive_case - проверка на удаление из избранного
10. test_get_list_of_favorites_books_positive_case - проверка на получение списка избранных книг
