class Student2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student2.count = Student2.count + 1

if Student2.count != 0:
    print('测试失败1!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print('测试失败2!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student2.count)
            print('测试通过!')


