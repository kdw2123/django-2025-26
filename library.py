class Library:
    def __init__(self):
        self.book = []
    def add_book(self,title):
        self.book.append(title)
        print(f"book {title}")
    def show_book(self):
        if self.book:
            print("books in th library : ")
            for book in self.book:
                print("-", book)
        else :
            print("nothin in here ")
obj = Library()
obj.add_book("maths")
obj.add_book("chemistry")
obj.add_book("find you elenent")
obj.show_book()