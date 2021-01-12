# coding: utf-8
# 使用while迴圈，計算1~某數字的總和
x = 0
sum = 0
stop = int(input("請輸入一個數字="))
while x!=stop:
	x+=1
	sum=sum+x
print("1加到{}等於={}".format(stop, sum))