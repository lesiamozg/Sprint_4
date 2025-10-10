import pytest
from main import BooksCollector

# Добавлены позитивные проверки для get_books_genre и get_list_of_favorites_books

@pytest.fixture
def collector():
    return BooksCollector()


# --- add_new_book ---
def test_add_new_book_adds_book_without_genre(collector):
    collector.add_new_book("Гарри Поттер")
    assert collector.get_book_genre("Гарри Поттер") == ''


@pytest.mark.parametrize("book_name", [
    "",                # пустая строка — не добавляем
    "A" * 41          # длиннее 40 символов — не добавляем
])
def test_add_new_book_invalid_length_not_added(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name not in collector.get_books_genre()


def test_add_new_book_duplicate_not_added_twice(collector):
    collector.add_new_book("Ведьмак")
    collector.add_new_book("Ведьмак")
    # словарь не должен содержать два элемента с одинаковым ключом
    assert len(collector.get_books_genre()) == 1


# --- set_book_genre ---
def test_set_book_genre_success(collector):
    collector.add_new_book("Властелин колец")
    collector.set_book_genre("Властелин колец", "Фантастика")
    assert collector.get_book_genre("Властелин колец") == "Фантастика"


@pytest.mark.parametrize("invalid_genre", [
    "Роман",
    "Биография"
])
def test_set_book_genre_invalid_genre_not_changed(collector, invalid_genre):
    collector.add_new_book("Книга без жанра")
    collector.set_book_genre("Книга без жанра", invalid_genre)
    # жанр не должен измениться (остается пустая строка)
    assert collector.get_book_genre("Книга без жанра") == ''


def test_get_book_genre_nonexistent_returns_none(collector):
    assert collector.get_book_genre("НеСуществующаяКнига") is None


# --- get_books_with_specific_genre ---
def test_get_books_with_specific_genre_returns_correct_books(collector):
    collector.add_new_book("Оно")
    collector.set_book_genre("Оно", "Ужасы")
    collector.add_new_book("Грот")
    collector.set_book_genre("Грот", "Ужасы")
    collector.add_new_book("Шерлок")
    collector.set_book_genre("Шерлок", "Детективы")

    result = collector.get_books_with_specific_genre("Ужасы")
    assert set(result) == {"Оно", "Грот"}


# --- get_books_for_children ---
def test_get_books_for_children_excludes_age_restricted_and_without_genre(collector):
    # возрастной рейтинг — Ужасы и Детективы
    collector.add_new_book("Оно")
    collector.set_book_genre("Оно", "Ужасы")  # возрастной — не для детей

    collector.add_new_book("Король Лев")
    collector.set_book_genre("Король Лев", "Мультфильмы")  # для детей

    collector.add_new_book("КнигаБезЖанра")  # без жанра — не должна попадать в список для детей

    children_books = collector.get_books_for_children()
    assert set(children_books) == {"Король Лев"}


# --- favorites ---
def test_add_book_in_favorites_and_get_list(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]


def test_add_book_in_favorites_cannot_add_twice(collector):
    collector.add_new_book("Ведьмак")
    collector.add_book_in_favorites("Ведьмак")
    collector.add_book_in_favorites("Ведьмак")
    assert collector.get_list_of_favorites_books() == ["Ведьмак"]


def test_add_book_in_favorites_only_if_book_exists(collector):
    # попытка добавить в избранное книги, которой нет в books_genre — не добавляем
    collector.add_book_in_favorites("НеСуществующаяКнига")
    assert collector.get_list_of_favorites_books() == []


def test_delete_book_from_favorites(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
    assert collector.get_list_of_favorites_books() == []
def test_get_books_genre_returns_correct_genre():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фэнтези")

    result = collector.get_books_genre("Гарри Поттер")
    assert result == "Фэнтези", "Метод get_books_genre должен возвращать корректный жанр книги"


def test_get_list_of_favorites_books_returns_correct_list():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Шерлок Холмс")
    collector.add_book_in_favorites("Гарри Поттер")

    result = collector.get_list_of_favorites_books()
    assert result == ["Гарри Поттер"], "Метод get_list_of_favorites_books должен возвращать список избранных книг"

def test_get_books_genre():
    collector = BooksCollector()
    collector.add_new_book("Книга 6")
    collector.set_book_genre("Книга 6", "Комедии")
    books_dict = collector.get_books_genre()
    assert books_dict == {"Книга 6": "Комедии"}

def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book("Фаворит 1")
    collector.add_new_book("Фаворит 2")
    collector.add_book_in_favorites("Фаворит 1")
    collector.add_book_in_favorites("Фаворит 2")
    fav_list = collector.get_list_of_favorites_books()
    assert fav_list == ["Фаворит 1", "Фаворит 2"]
