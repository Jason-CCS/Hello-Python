def flippingMatrix(matrix):
    # Write your code here
    length = len(matrix)
    n = int(length / 2)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += max([matrix[i][j], matrix[i][2 * n - 1 - j], matrix[2 * n - 1 - i][j],
                        matrix[2 * n - 1 - i][2 * n - 1 - j]])
    return sum


print(max([234, 234, 234, 555]))

matrix = [[112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]

print("the biggest sum is {}".format(flippingMatrix(matrix)))
