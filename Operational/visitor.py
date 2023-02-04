
class CoursesAtSDA:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__


class School1(CoursesAtSDA): pass


class School2(CoursesAtSDA): pass


class School3(CoursesAtSDA): pass


class Visitor:

    def __str__(self):
        return self.__class__.__name__


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)


s1 = School1()
s2 = School2()
s3 = School3()

instructor = Instructor()
student = Student()

s1.accept(instructor)
s1.accept(student)

s2.accept(instructor)
s2.accept(student)

s3.accept(instructor)
s3.accept(student)
