# # import my_module as mm
#
# from my_module import sayHello
# from my_module import pi
#
#
# sayHello('David')
# print(pi)
#
# # print(student_data['name'])














# class MyClass:
#     x = 5
#
# obj = MyClass()
#
# print(obj.x)








class Person:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age

    def greeting(x):
        print(f'Hi, {x.name}')

# p1 = Person('David', '80')
#
# print(f'Age: {p1.age}')
# print(f'Name: {p1.name}')
# p1.greeting()
#
# print()
# p2 = Person('Kosi', '100')
#
# print(f'Age: {p2.age}')
# print(f'Name: {p2.name}')
# p2.greeting()

# inheritance

class Student(Person):
    def __init__(self, name, age, reg_no):
        Person.__init__(self, name, age)
        # or
        # super().__init__(name, age)
        self.reg_no = reg_no

    def studentData(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Reg no: {self.reg_no}')

s1 = Student('david', '100', 'cs123')

s1.studentData()
print()

s1 = Student('Emma', '20', 'cs5523')

s1.studentData()