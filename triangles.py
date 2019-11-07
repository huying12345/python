# 切片
# 利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，注意不要调用str的strip()方法：
# 使用递归函数
def trim(str):
    if(str==''):
        return str
    elif (str[0]!=' ') and (str[-1]!=' '):
        return str
    elif str[0]==' ':
        return trim(str[1:])
    else :
        return trim(str[0:-1])

# 验证一个值是否是可迭代的对象，关键字Iterable，取出对象中的最大最小值
from collections import Iterable
def findMainAndMax(L):
	if len(L) == 0:
		print(None,None)
	elif isinstance(L, Iterable):
		m = L[0]
		M = L[0]
		for s in L:
			if s < m:
				m = s
			else:
				M = s
		print(m,M)
	else:
		print(None,None)
