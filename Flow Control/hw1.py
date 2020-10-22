"""
homework:
連續輸入五次兩個數字，
x=?
y=?
並且每次皆印出x>y or x<y or x==y
"""
print("請輸入，x=")
x=int(input())
print("x =",x)
print("請輸入，y=")
y=int(input())
print("y =",y)
if x==y:
    print("x=y")
if x>y:
    print("x>y")
if x<y:
    print("x<y")