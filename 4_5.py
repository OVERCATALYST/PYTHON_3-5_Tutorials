class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name, "Age:", self.age, "Salary:", self.salary)

p1 = Person("Alice", 30, 50000)
p2 = Person("Bob", 35, 60000)
p1.display()
p2.display()
