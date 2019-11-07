from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))

# => 利用匿名函数（lambda)简化

def char2num(s):
	return DIGITS[s]

 def str2int(s):
 	return reduce(lambda x,y:x*10+y, map(char2num,s))

str2int('123243') #123243




# name.title()  首字符大写

def fn(names):
	return list(map(lambda name : name.title(), names))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
def str2float(s):
	nums = map(lambda x : CHAR_TO_FLOAT(x), s)
	point = 0
	def to_float(f, n):
		nonlocat point
		if n == -1:
			point = 1
			return f
		if point == 0:
			return f * 10 + n
		else:
			point = point * 10
			return f + n / point
	return reduce(to_float, nums, 0.0)
	 

