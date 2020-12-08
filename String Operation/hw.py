# 印出聖誕樹

step = 4
layer = 5
level = 3

for i in range(level):
    startNumber = i * 2 + 1
    endNumber = startNumber + layer * step
    for j in range(startNumber, endNumber, step):
        stars = '*' * j
        print(stars.center(100, ' '))

for k in range(5):
    stars = '*' * 5
    print(stars.center(100, ' '))