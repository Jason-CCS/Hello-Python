# coding: utf-8
"""
試著將一個班級有["Bill", "Doris", "Ace", "Carol", "Florence", "Ethan"]的List
六個同學依照字母多寡，由少排至多印出，相同字母數的前後不拘，
所以結果會是=>["Ace", "Bill", "Doris", "Carol", "Ethan", "Florence"]
"""

"""
策略一：比六次，每次將最短的取出來，存入到新的list，並將此元素從舊班級刪除掉
"""
cls=["Bill", "Doris", "Ace", "Carol", "Florence", "Ethan"]
print(cls)
newCls=[]
for i in range(len(cls)):
	minName=cls[0]
	for x in cls:
		if len(minName) > len(x):
			minName = x
	newCls.append(minName)
	cls.remove(minName)
print(newCls)

"""
策略二:Bubble sort，操作索引
"""
cls=["Bill", "Doris", "Ace", "Carol", "Florence", "Ethan"]
for i in range(len(cls)):
	minIndex=i
	for j in range(i+1, len(cls)):
		if len(cls[i]) > len(cls[j]):
			minIndex=j
	cls.insert(i,cls.pop(minIndex))
print(cls)












