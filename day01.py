# # 命名元组
#
# from collections import namedtuple
# tu = ("dsw", 27, 'man')
# student_info = namedtuple('student_info', ['name', 'age', 'gender'])
#
# tu_1 = student_info('dsw', 27, 'male')
# print(tu_1)
# print(tu_1.name)
# print(tu_1.age)
# print(tu_1.gender)
# print(type(tu_1))
#
# # 字典集合{}
# se = set()   # 空集合
# set1 = {1, 2, 3}  # 去重功能
# dic = {}   # 空字典
#
# # 集合添加数据 集合可变的 无序
# set1.add(666)
# set1.remove(1)
# set1.update({111, 222, 333})
# set1.clear()
# set1.copy()
# print(set1)
#

# () 生成器表达式
tu = (i for i in range(10))
print(tu)
a = next(tu)  # 取下一个 节省内存 提高性能
print(a)


# 通过yield定义生成器 返回生成器对象
def get_fun():
    yield 10
    print('AAA')
    yield 100
    print('BBB')
    yield 1000
    print('CCC')
    yield 10000
    print('DDD')


res = get_fun()
print(next(res))
print(next(res))

li = [1, 2, 3, 4]
li1 = iter(li)
print(next(li1))
print(next(li1))
print(next(li1))
print(next(li1))
print(next(li1))
