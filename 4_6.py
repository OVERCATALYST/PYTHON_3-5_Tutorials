class Mobile:
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print("Company:", self.company, "Model:", self.model, "Price:", self.price)

m = Mobile()
m.set_details("Samsung", "S22", 75000)
m.display_details()
