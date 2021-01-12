# coding: utf-8
# homework:
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

def prod(list):
	def multiply(x, y):
		return x * y
	return reduce(multiply, list)

print(prod([2, 123, 34, 2]))