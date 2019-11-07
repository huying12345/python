# 生成一个以3开头的基数序列  生成器并且是个无限序列
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n

# 定义一个筛选函数
def _not_divisible(n):
	return lambda x : x%n >0  # 匿名函数  参数x return x%n>0

# 定义一个生成器  不断返回下一个素数  无线序列
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n=next(it)
		yield n
		it = filter(_not_divisible(n), it)

# 打印1000以内的素数

for n in primes():
	if n<1000:
		print(n)
	else:
		break

# 打印回数：指从左向右读和从右向左读都是一样的数
# s[0]=s[-1]
# s[1]=s[-2]
# s[2]=s[-3]
# s[n]=s[n-(n+1)]

def is_backFn(s):
	n = int(str(s)[::-1])  #12345 => 54321
	return n == s

filter(is_backFn, range(1,1000))


