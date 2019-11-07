def createCounter():
	def counter():
		global n #全局变量
		n=n+1
		return n
	return counter  #每次调用子函数，都是会保留上次s的值进行计算的
