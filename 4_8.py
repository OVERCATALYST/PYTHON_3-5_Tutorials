class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print("Title:", self.title, "Author:", self.author, "Cost:", self.cost)

b = Book()
b.get_details("Python Basics", "John Doe", 450)
b.print_details()
