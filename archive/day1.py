# coding: utf-8
# 宣告上面那一行，說明是哪一種編碼法

""" Syntax 語法 """
# print("Hello World～");
# print("This is Python.")

# 使用縮排（空白符）來區分code block
# if 5<2:
 # print("11111")
# print("22222")

# if 5>2:
  # print("5>2")
  # if(5<2):
  	# print("la;kdjsf;jsd;flj")
  # print("3333333")

# if 5>2:
	# print("5>2")
# if 100>11:
	# print("alkdsjflksdfjlk")

# 註解
# this is comment 這是單行註解
""" this is multi-line
這是多行註解
jlk;asjdfkl;ja;lsdfjka
alksjdfkj
For me to see only.
command"""

# """ 變數 """
# 宣告變數無需特別識別字，如php需要 $x=5;, js需要 var x = 5; java 需要 int x = 5
# x=5
# y=2
# if x>y:
# 	print("x is greater than y")

# x="this is text"
# print(x)

# 變數是大小寫有差的
# x=5
# X=51
# if x!=X:
# 	print("x is not equal to X")

""" 型別 """
# 數字的型別有三： int, float, complex
# print(type(1))
# print(type(1.0))
# print(type(1j))

# x = 3+5j
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))
# print(type(z))

# casting 轉型
# x = int(1)		 # x will be 1
# x = float(1)     # x will be 1.0
# y = int(2.8)	 # y will be 2
# y = float(2.8)   # y will be 2.8

# print("float('3')=")
# print(float('3'))

# 字串型別
# s = "Hello, this is String."

""" string 字串操作 """
# s = "Hello, World!"
# print(s[2:6]) # 子字串
# print(len(s)) # 字串長度
# print(s.replace("o", "OOO")); # 取代
# print(s.split(",")[1]) # 切割

# console輸入
# print("請輸入你的名字")
# name=input()
# print("嗨，" + name)

""" Operators 運算子 """
# Arithmetic Operators 算數運算子
x=3
y=5
print("x*y=")
print(x+y)
print("x/y")
print(x/y)

# Assignment Operators 指派運算子
x=3
print("x=3")
x+=3 
print("x+=3")
print("x=")
print(x)

# # Comparison Operators 比較運算子
x=3
y=5
print(x==y)
print(x>y)
print(x<y)
print(x!=y)

# Logical Operators 邏輯運算子
print("check if x==y or x>y:")
print(x==y and x>y)

# Identity Operators 本身運算子
x=3
y=3
print("check if x is y:")
print(x is y)

# Membership Operators
x = ["apple", "banana"]
print("kite" in x)



