"""
homework:
連續輸入五次兩個數字，
x=?
y=?
並且每次皆印出x>y or x<y or x==y
"""
for i in range(5):
    x = int(input('請輸入x='))
    print('x={}'.format(x))
    y = int(input('請輸入y='))
    print('y={}'.format(y))
    if x == y:
        print("x==y")
    if x > y:
        print("x>y")
    if x < y:
        print("x<y")
