class Student:
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print("Roll No:", self.rollno, "Mark1:", self.mark1, "Mark2:", self.mark2, "Total:", self.total)

s = Student()
s.readData(101, 85, 90)
s.computeTotal()
s.printDetails()
