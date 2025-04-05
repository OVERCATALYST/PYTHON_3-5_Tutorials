class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def dataprint(self):
        print("Name:", self.name, "Roll No:", self.roll)

s1 = Student("Anu", 1)
s2 = Student("Manu", 2)
s1.dataprint()
s2.dataprint()
