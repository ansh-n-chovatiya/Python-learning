class Book:
    title = ""
    author = ""
    isbn = None
    is_available = True

    def __init__(self, config={
        "is_available": True
    }):
        self.title = config["title"]
        self.author = config["author"]
        self.isbn = config["isbn"]
        self.is_available = config["is_available"]

    def checkout():
        pass

    def return_book():
        pass


class EBook(Book):

    def __init__(self, config={"is_available": True}):
        super().__init__(config)
        self.file_size_mb = config["file_size_mb"]

    def __str__(self):
        return self.title
