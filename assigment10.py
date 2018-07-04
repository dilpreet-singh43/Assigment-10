
class Animal:
    def animal_attribute(self):
        print("This is an Animal Class")
class  Tiger(Animal):
    def display(self):
        print("This is the Lion Class")

a= Tiger()
a.animal_attribute()
a.display()


'''Ques 2. What will be the output of following code.'''
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()'''
# Solution
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())




'''Ques 3. Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add,
display and update the following details. Create another class Mission which extends the class Cop. Define method
add_mission _details. Select an object of Cop and access methods of base class to get information for a particular
 cop and make it available for mission.'''
class Cop:
    def add(self,name,age,work_experience,designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation
    def display(self):
        print("\n\nDetails Will be:")
        print("\nName is: ",self.name)
        print("\nAge is: ",self.age)
        print("\nWork_Experience: ",self.work_experience)
        print("\nDestination: ",self.designation)
    def update(self,name,age,work_experience,designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation
class Mission(Cop):
    def add_mission_details(self,mission):
        self.mission=mission
        print(self.mission)
m=Mission()
m.add_mission_details("Mission detail Assigned to HP :")
m.add("Dilpreet",18,8,"worker\n")
m.display()
m.update("Faizal",21,2,"worker")
m.display()

   
   
   
   
'''Ques 4. Create a class Shape.Initialize it with length and breadth Create the method Area.
Create class rectangle and square which inherits shape and access the method Area.'''
class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        self.area = self.length * self.breadth
class Rectangle(Shape):
    def area_rectangle(self):
        print("Area of Rectangle is :", self.area)
class Square(Shape):
    def area_square(self):
        print("Area of Square is :", self.area)
length = int(input("Enter the Length:"))
breadth = int(input("Enter the Breadth:"))
a = Rectangle(length,breadth)
b = Square(length,breadth)
if length == breadth:
    b.area()
    b.area_square()
else:
    a.area()
    a.area_rectangle()