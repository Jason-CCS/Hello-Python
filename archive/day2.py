# coding: utf-8

""" List """
# List我們又稱為串列，是一組資料形成的資料陣列，其中資料之間是可以重複的，而且資料可以被增刪改查。
# CRUD(Create, Read, Update, Delete)
# ex.
# ["Jason", "Ken", "Lucy"]
#	  0		  1		  2		<-- 索引值

# Create創造串列
# 我們說我們現在有一個部落格，部落格當中有很多會員，
# members=["Jason", "Ken", "Lucy"]
# print(members)

# # 增加會員
# # 加到串列最後方，就像排隊一樣
# members.append("Carol") 
# print(members)
# # 插隊，插入第二個
# members.insert(1, "Grace")
# print(members)

# # 讀取List中某值 Read
# # 取得第三個會員的值
# print(members[2])
# # 取得前兩個會員的值
# print(members[0:2])

# # 修改List中某值 Update
# # 第二個會員改名字，改成Kid
# members[1]="Kid"
# print(members)

# # 刪除List中某值 Delete
# # 直接刪除某值
# members.remove("Kid")
# # 將某索引的值取出，沒有指定索引的話，就是將最後一個取出
# print(members)
# print(members.pop(0))
# print(members)
# # 清除整個串列
# members.clear()
# print(members)
# members=["Jason", "Ken", "Lucy"]

# # 其他函式
# # 取得某會員的索引值
# print(members.index("Jason"))

# # 檢查該會員是否存在
# who=input("請輸入名字")
# if who in members:
# 	print("有此會員")
# else:
# 	print("無此會員")

# # 總共有多少會員
# print("總共有"+str(len(members))+"個會員" )

""" for迴圈 """
# for迴圈是用來對各種資料結構進行遍歷的，也就是巡視Iterate。
# 其中資料結構在程式語言當中我們稱之為Collection，而在電腦科學當中有一門課叫做資料結構，
# 專門在教資料結構原理。
# Python的Collection包含List, Tuple, Set, Dictionary
# 所以什麼是迴圈？
# 舉例來說：
# members = ["Jason", "Ken", "Lucy”] List，就會按照索引的順序取出
# members = ["Jason", "Ken", "Lucy", "Mary", "Ned"]
# print(members)
# for oneOfMember in members:
# 	print(oneOfMember)

# # String 也可以被遍歷
# for x in "abcdefg":
# 	print(x)

# # 中斷迴圈 保留字：break
# for x in members:
# 	print(x)
# 	if x=="Ken":
# 		print("we got Ken")
# 		break
# 	print("-------")

# # 下一個迴圈繼續 保留字:continue
# for x in members:
# 	if x=="Lucy":
# 		continue
# 	print(x)
# 	print("-------")

# # range() class
# print(list(range(5)))
# print(list(range(1,5)))
# # 常被用在迴圈當中
for x in range(3):
	print(x)

# 迴圈當中的else保留字，迴圈結束後執行
for x in range(6):
	print(x)
	if x==4:
		break
else:
    print("Finally finished!")

# 槽狀迴圈
adj=["cool", "great", "nice"]
for x in adj:
	for y in members:
		print(x, y)
