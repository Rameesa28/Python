class rectangle:
    def getdata(self):
        self.a=int(input("enter length:"))
        self.b=int(input("enter breadth:"))
    def area(self):
        area=self.a*self.b
        print("area:",area)
        return(area)
    def perimeter(self):
        perim=2*(self.a+self.b)
        print("perimeter:",perim)
        return(perim)
print("1sr rectangle")
ob1=rectangle()
ob1.getdata()
a1=ob1.area()
p1=ob1.perimeter()
print("\n2nd rectangle")
ob2=rectangle()
ob2.getdata()
a2=ob2.area()
p2=ob2.perimeter()
if a1==a2:
    print("\nareas are equal")
elif a1>a2:
    print("\narea of 1st rectangle greater 2nd rectangle")
else:
    print("\narea of 1st rectangle")
