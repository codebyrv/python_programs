
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):

    def __init__(self, name, age, exp, r_area):
        super().__init__(name, age)

        self.exp = exp
        self.r_area = r_area

    def displayData(self):
        super().display()

        print("Experience:", self.exp)
        print("Research area:", self.r_area)


class Student(Person):

    def __init__(self, name, age, course, marks):
        super().__init__(name, age)

        self.course = course
        self.marks = marks

    def displayData(self):
        super().display()

        print("Course:", self.course)
        print("Marks:", self.marks)


print("******** TEACHER ********")

T = Teacher("Rijo", 43, 20, "Recommended Systems")
T.displayData()


print("******** STUDENT ********")

S = Student("Mani", 20, "BTech", 78)
S.displayData()




print("T is a Teacher:",isinstance(T,Teacher))
print("T is a Person:",isinstance(T,Person))
print("T is a integer:",isinstance(T,int))
print("T is a object:",isinstance(T,object))
print("perosn is a subclass of teacher",issubclass(Person,Teacher))
print("teacher is a subclass of person",issubclass(Teacher,Person))
print("boolean is a subclass of int",issubclass(bool,int))


