
# python内置方法之enumerate(iterable, start=0)
# 实现原理如下：
def enumerate(sequence, start=0):
	n = start
	for elem in sequence:
		yield n, elem
		n += 1

# python编译器
>> from enumerate import enumerate
>> list = enumerate(('Spring', 'Summer', 'Fall', 'Winter'))
>> list
<generator object enumerate at 0x000001763EFE6B88>
>> list.__next__()
(0, 'Spring')
>> list.__next__()
(1, 'Summer')
>> list2 = enumerate(['Spring', 'Summer', 'Fall', 'Winter'], 10)
>> list2.__next__()
(10, 'Spring')
>> list2.__next__()
(11, 'Summer')

# 默认start从0开始，自定义start值也可以

