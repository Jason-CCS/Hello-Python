# coding: utf-8
# 請連續輸入五位同學英文名字，並找出英文字母數最多的同學，舉例如下：
# Bill
# Doris
# Ace
# Florence
# Ethan
# 則print(max)會印出，Florence
cls=[]
for i in range(5):
	cls.append(input("請輸入名字="))

print(cls)

maxName=cls[0]
for x in cls:
	if len(x)>len(maxName):
		maxName=x

print(maxName)



