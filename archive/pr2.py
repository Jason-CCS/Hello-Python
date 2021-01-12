# coding: utf-8
# 試著將連續輸入三次的資料存入List並倒序印出
l=[]
m=[]
for x in range(3):
	l.append(input("請輸入"))
print(l)
for x in range(len(l)):
	m.append(l.pop())
print(m)

