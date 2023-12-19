class Student:
    def __init__(self,rlno,name):
        self.rlno=rlno
        self.name=name
    def display(self):
        print("rollno:",self.rlno)
        print("name:",self.name)

stud1=Student(10,"Rameesa")
stud1.display()
