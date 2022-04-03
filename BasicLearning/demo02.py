# # f format
# dict_person = {
#     'name': 'DedicationYu',
#     'age': 23,
#     'sex': 'male'
# }
# print(f"my name is {dict_person['name']}, I am {dict_person['age']} years old ")
# # my name is DedicationYu, I am 23 years old


# # Sort the dictionaries in the list by the value of a certain key
# grades_students = [
#     {'name': 'Alice', 'age': 23, 'grade': 98},
#     {'name': 'Bob', 'age': 22, 'grade': 99},
#     {'name': 'Dave', 'age': 24, 'grade': 95},
#     {'name': 'DedicationYu', 'age': 23, 'grade': 99},
#     {'name': 'Meiko', 'age': 22, 'grade': 95},
# ]
# for out in range(len(grades_students)-1):
#     for in_ in range(out+1, len(grades_students)):
#         if grades_students[out]['grade'] < grades_students[in_]['grade']:
#             grades_students[out], grades_students[in_] = grades_students[in_], grades_students[out]
# print(grades_students)


# # list comprehension nesting
# # All possible outcomes of a roll of two dice
# list01 = []
# list02 = []
# for num in range(1, 7):
#     list01.append(str(num))
#     list02.append(str(num))
# result = [lis01 + ' ' + lis02 for lis01 in list01 for lis02 in list02]
# print(result)


# # Actual parameters and formal parameter
# def func01(*p1):
#     """
#     *p1 Indicates an unlimited number of real parameters, Only positional real parameters are supported
#     """
#     print(p1)
#
#
# def func02(**p2):
#     """
#     **p2 Indicates an unlimited number of real parameters, Only real parameters with keywords are supported
#     :param p2:
#     :return:
#     """
#     print(p2)
#
#
# func01(1, 2)  # (1, 2)  tuple
# func02(a = 1, b = 2)  # {'a': 1, 'b': 2}  dictionary


# # global variable
# glob01 = 10
# glob02 = [1, 2]
#
#
# def func03():
#     """
#     glob01 is a global variable, pointing to 10 in memory. glob01=20 means modify the global variable pointing to 20,
#     the function can not modify the global variable, need to add global.
#     """
#     global glob01
#     glob01 = 20
#
#
# def func04():
#     """
#     glob02 is a global variable that points to a list in memory,
#     the first element of the list points to 1 and the second element points to 2.
#     glob02[0]=3 means that the first element of the list is modified to point to 3.
#     This operation modifies the list and does not modify the global variable, so there is no need to add global.
#     """
#     glob02[0] = 3
#
#
# func03()
# func04()
# print(glob01)  # 20
# print(glob02)  # [3, 2]


# def glob05(p1, p2):
#     print(p1, end=' ')
#     print(p2, end=' ')
#
# args = [2, 3]
# glob05(*args)  # The container is split into multiple real parameters, here are the location parameters  2 3
# kwargs = {
#     'p2': 11,
#     'p1': 23,
# }
# glob05(**kwargs)  # The container is split into multiple real parameters, here are the keyword real parameters  23 11


# """
# Order of parameters from left to right:
# Position formal parameter --> asterisk tuple formal parameter -->
# named keyword formal parameter --> double asterisk dictionary formal parameter
# """
#
#
# def func05(*args, p1):
#     """
#     :param args: asterisk tuple formal parameter
#     :param p1: named keyword formal parameter
#     :return:
#     """
#     print(args)  # (1,)
#     print(p1)  # 2
#
#
# def func06(p1,*, p2):
#     """
#     Separated by *, the former indicates the position formal parameter, the latter indicates the keyword formal parameter
#     :param p1: Position formal parameter
#     :param p2: named keyword formal parameter
#     :return:
#     """
#     print(p1)  # 3
#     print(p2)  # 4
#
#
# func05(1, p1=2)
# func06(3, p2=4)

