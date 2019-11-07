# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

from operator import itemgetter  #itemgetter函数用于获取对象的哪些维的数据

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return itemgetter(0)

sorted(L, key=by_name)  #按名字排序

sorted(L, key=lambda x : x[1])  #按成绩排序

sorted(L, key=itemgetter[1], reverse=True)  #按成绩的倒序排序
