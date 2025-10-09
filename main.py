# Minor update for review

class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = [
            'Фантастика', 'Детективы', 'Ужасы',
            'Комедии', 'Фэнтези', 'Мультфильмы'
        ]

    def add_new_book(self, name):
        if 1 <= len(name) <= 40 and name not in self.books_genre:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        return self.books_genre.get(name)

    def get_books_genre(self, name=None):
        # Если указан конкретный book_name — вернуть его жанр
        if name:
            return self.books_genre.get(name)
        # Если без аргумента — вернуть весь словарь
        return self.books_genre

    def get_books_with_specific_genre(self, genre):
        return [book for book, g in self.books_genre.items() if g == genre]

    def get_books_for_children(self):
        forbidden = ['Ужасы']
        return [
            book for book, genre in self.books_genre.items()
            if genre not in forbidden and genre != ''
        ]

    def add_book_in_favorites(self, name):
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        return self.favorites
