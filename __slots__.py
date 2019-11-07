class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)  #'Michael'

# 给实例添加方法
def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # MethodType(arg1, arg2) arg1是方法名，arg2是实例名
s.set_age(30)
s.age  # 30



