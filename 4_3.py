class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print("Model:", self.model, "Year:", self.year, "Price:", self.price)

car1 = Car("Toyota", 2020, 800000)
car2 = Car("Honda", 2022, 950000)
car1.cost()
car2.cost()
