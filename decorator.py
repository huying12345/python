import time, functools

def metric(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('%s executed %s'%(func.__name__, 10.24))
		return func(*args, **kw)
	return wrapper

@metric
def fast(x, y):
	time.sleep(0.0013)
	return x+y;

@metric
def slow(x,y,z):
	time.sleep(0.1234)
	return x*y*z;

f = fast(11,22)
s = slow(11,22,33)
if f != 33:
	print('测试失败')
elif s != 7986:
	print('测试失败')
else:
	print('测试成功')

# fast executed 10.24
# slow executed 10.24
# 测试成功
