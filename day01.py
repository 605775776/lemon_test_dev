# 命名元组

from collections import namedtuple
tu = ("dsw", 27, 'man')
student_info = namedtuple('student_info', ['name', 'age', 'gender'])

tu_1 = student_info('dsw', 27, 'male')
print(tu_1)
print(tu_1.name)
print(tu_1.age)
print(tu_1.gender)
print(type(tu_1))