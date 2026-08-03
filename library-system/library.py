class Library:
    book_list = []

    def __init__(self, book_list):
        self.book_list = book_list

    def add_book(self, book):
        self.book_list.insert(0, book)

    def find_by_title(self, title):

        book = None

        for item in self.book_list:
            print(item)
