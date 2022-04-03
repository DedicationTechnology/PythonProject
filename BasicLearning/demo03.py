# """
# property
# principle:One private variable, two public methods
# """
# class Chinese:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # shortcut key: prop + enter
#     @property  # @property:Turn instance properties into attributes, in this case private properties, get private variable
#     def age(self):  # function name must be the property name
#         return self.__age
#     @age.setter  # @property name.setter:change private variable
#     def age(self, value):  # function name must be the property name
#         if value <= 0 or value >= 100:
#               raise Exception('The age you entered does not match the reality')
#         else:
#             self.__age = value
#
#
# DedicationYu = Chinese('DedicationYU', 80)
# DedicationYu.age = 23  # change private variable
# print(DedicationYu.age)  # get private variable


# class Vector:
#     """
#     Custom Class
#     """
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def __add__(self, other):
#         """
#         Two classes can be added together because of the __add__ method
#         The reason why two variables of type int can be added is that the int class has the __add__ method
#         :param other:  Another summation class
#         :return:
#         """
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#
#     def __str__(self):
#         """
#         Changing the default return value of a class
#         :return:
#         """
#         return f'Vector{self.x , self.y}'
#
# num1 = Vector(1, 2)
# num2 = Vector(3, 4)
# num1 += num2
# print(num1)


"""
    type tagging(explanatory note)
        grammar：
            variable: type
            def FunctionName()->type:
            self.InstanceVariable = Data # type: Type
"""

# # First. Marking Parameters
# def func01(data: int):
#     print(data)
#
#
# func01("a")
#
#
# # Second. Mark Return Value
# def func02() -> int:
#     return 10
#
#
# re = func02()
# print(re)
#
#
# # Third. Mark Instance Variable
# class MyClass:
#     def __init__(self, data01):
#         self.data01 = data01  # type:int
#
#
# # Forth. Complex Type
# from typing import List, Tuple, Dict, Union, Optional
#
# # -- Container
# list01 = []  # type:List[str]
# tuple01 = ("a",)  # type:Tuple[str]
# dict01 = {}  # type:Dict[str,float]
#
#
# # -- Mark Multiple Types
# def func03(a: Union[int, str]):
#     print(a)
#
#
# # -- Optional type (can be passed without information)
# def func04(a: Optional[int, str] = ""):
#     print(a)
#
#
# func04()


# # fibonacci sequence of numbers
# def fibonacci(n):
#     front, behind, count = 0, 1, 0
#     while count < n:
#         # Functions That Use Yield Are Called Generators
#         yield front  # yield Equivalent To return
#         front, behind = behind, front + behind
#         count += 1
#
# # transfer the generator function will automatically create the iterator object
# iterator1 = fibonacci(10)
# while True:
#     try:
#         """
#         The generator function is executed only when the __next__() method of the iterator object is transfered.
#         Return the data each time the execution reaches the yield statement and leave temporarily.
#         Continue execution from where it left off when the __next__() method is transfered next time.
#         """
#         print(next(iterator1), end=' ')
#     except StopIteration:  # Ends the loop when the iterator stops iterating
#         break


# # matrix transposition
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# """
# The zip() function takes an iterable object as a parameter, packs the corresponding elements of the object into a tuple,
# and returns the object composed of these tuples
# """
# list02 = [list(item) for item in zip(*list01)]  # In contrast to zip, zip(*) can be interpreted as decompression
# print(list02)  # >>> [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]


# list01 = [1, 2, 3]
# list02 = [4, 5, 6, 7]
# # If the number of elements in each iterator is not the same, the list length is the same as the shortest object
# list03 = list(zip(list01, list02))
# print(list03)  # >>> [(1, 4), (2, 5), (3, 6)]
# # In contrast to zip, zip(*) can be interpreted as decompression
# list04 = [list(li) for li in zip(*zip(list01, list02))]
# print(list04)  # >>> [[1, 2, 3], [4, 5, 6]]


# class Employee:
#     def __init__(self, eid, did, name, money):
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employees = [
#     Employee(1001, 9002, "Alice", 60000),
#     Employee(1002, 9001, "Bob", 50000),
#     Employee(1003, 9002, "Crime", 20000),
#     Employee(1004, 9001, "Dave", 30000),
#     Employee(1005, 9001, "DedicationYu", 15000),
# ]
#
#
# # Exercise 2: Define the function to find all employees with a salary greater than 50000 in the employee list
# def find_employee_by_money():
#     for item in list_employees:
#         if item.money > 50000:
#             yield item
#
#
# for emp in find_employee_by_money():  # for traverse can realise __next__ method, emp equivalent to item
#     print(emp.__dict__)  # __dict__： A property of the object of the class, used to store a dictionary of its own instance variables
#     # >>> {'eid': 1001, 'did': 9002, 'name': 'Alice', 'money': 60000}


# # variable = lambda formal parameter: method body
# def func01(name):
#     print(name)
#
#
# func01('DedicationYu')  # >>> DedicationYu
#
#
# func02 = lambda name: print(name)
#
#
# func02('DedicationYu')  # >>> DedicationYu
import time

"""
announcements:
First. Assignment statements are not supported
Second. Multiple statements are not supported
"""

#
# class Employee:
#     def __init__(self, eid, did, name, money)
#         self.eid = eid
#         self.did = did
#         self.name = name
#         self.money = money
#
#
# list_employees = [
#     Employee(1001, 9002, "Alice", 60000),
#     Employee(1002, 9001, "Bob", 50000),
#     Employee(1003, 9002, "Crime", 20000),
#     Employee(1004, 9001, "Dave", 30000),
#     Employee(1005, 9001, "DedicationYu", 15000),
# ]
# """
# map(): map (function, iterable object): transfer the function using each element of the iterable object,
# and return the value as the new iterable object element; the return value of the map method is the new iterable object
# """
# # exercise: Get the names of all employees
# for name in map(lambda item: item.name, list_employees):
#     print(name, end=' ')  # >>> Alice Bob Crime Dave DedicationYu
#
# """
# filter(): filter(function, iterable object): filter the elements of the iterable object according to the conditions,
# the return value is the new iterable object
# """
# # exercise: Find employees whose department is 9002
# for message in filter(lambda diversion: diversion.did == 9002, list_employees):
#     print(message.__dict__, end=' ')  # >>> {'eid': 1001, 'did': 9002, 'name': 'Alice', 'money': 60000} {'eid': 1003, 'did': 9002, 'name': 'Crime', 'money': 20000}

"""
max(): max(iterable object, key = function): get the maximum value of the iterable object according to the function
"""
# exercise: Find the highest paid employees
# sal = max(list_employees, key=lambda salary: salary.money)
# print(sal.__dict__)

"""
sorted(): sorted(iterable object, key = function, reverse = bool value): sort, return value is the sorting result
"""
# list01 = sorted(list_employees, key= lambda salary: salary.money, reverse= True)
