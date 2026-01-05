"""
Никогда не используйте изменяемые объекты (списки, словари, множества)
как дефолтные аргументы.
"""


class MyClass:
    def __init__(self, a=[]):
        self.a = a


my_class_1 = MyClass()
my_class_1.a.append('1')

my_class_2 = MyClass()
my_class_2.a.append('2')

print(my_class_1.a)
print(my_class_2.a)
