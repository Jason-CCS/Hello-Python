# coding: utf-8

""" Tuple """
# Tuple跟List是類似的，但是tuple一經宣告，就無法再被改變，所以沒有增刪改，只有查
# 宣告Tuple
members=("Apple", "Banana", "Carrot")
print(members)

# 宣告一個空的tuple
t=()
print(t)

# 宣告一個只有一個元素的tuple
t=(3,)
print(t)

# 查
print(members[1])

# # 試著改變tuple
# members[0]="AAAAA"
# print(members)

# 遍歷Tuple
for x in members:
	print(x)

# 檢查是否存在
if "Carrot" in members:
	print("Carrot is in members")

# tuple的長度
print(len(members))

# 刪除tuple
del members

# tuple 函式
members=("Apple", "Banana", "Carrot", "Apple")

# 計算出現幾次
print(members.count("Apple"))

# 返回索引值
print(members.index("Apple"))

"""條件判斷"""
# x = int(input("x="))
# y = int(input("y="))

# if x>y:
# 	print("{} is greater than {}".format(x, y))
# elif x<y:
# 	print("{} is smaller than {}".format(x, y))
# elif x==y:
# 	print("{} is equal to {}".format(x, y))
# else:
# 	print("沒有條件符合，那就印這行")

"""while迴圈"""
# 列印 1 ~ 指定的數字
stop = int(input("number is:"))
i=0
while i<stop:
	i+=1
	print(i)

i=0
while i<stop:
	i+=1
	if i ==	5:
		break
	print(i)

i=0
while i<stop:
	i+=1
	if i ==	5:
		continue
	print(i)	


"""練習"""
# 終極密碼
# final = int(input("終極密碼是="))
# lb = 1
# ub = 1000
# while True:
# 	guess = int(input("你選擇的數字是="))
# 	if guess>final:
# 		ub=guess
# 	elif guess<final:
# 		lb=guess
# 	else:
# 		print("Bingo!!!")
# 		break
# 	print("終極密碼在{}和{}之間".format(lb, ub))



