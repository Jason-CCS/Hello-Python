def findNumberOfTriangle(number):
    counter = 0
    for i in range(1, number):
        if 2 * i <= number - 2 * i:
            last = 2 * i
        else:
            last = number - 2 * i
        for j in range(1, last):
            if j == i:
                continue
            print('(' + str(i) + ', ' + str(i) + ', ' + str(j) + ')')
            counter += 1
    return counter


print(findNumberOfTriangle(20))
