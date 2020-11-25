"""
使用串列，讓使用者可以連續輸入五位同學英文名字，找出英文字母數最多的同學，例如Bill, Doris, Ace, Florence, Ethan，最多的為Florence。
"""
names = []
for i in range(5):
    names.append(input("請輸入名字="))

print(names)

# 此為max旗標法，在許多演算法中，可以常見到，將所需要的值，固定的存在一個變數中
maxName = names[0]
for x in names:
    if len(x) > len(maxName):
        maxName = x

print('英文字母數最多的是{}'.format(maxName))

