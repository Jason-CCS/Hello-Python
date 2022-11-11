import math


def findMedian(arr):
    # Write your code here
    arr.sort()
    length = len(arr)
    return arr[math.floor(length / 2)]


def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    left_right_diagonal = 0
    right_left_diagonal = 0
    for i in range(n):
        print(arr[i][i])
        left_right_diagonal += arr[i][i]
        arr[i].reverse()
        print(arr[i][i])
        right_left_diagonal += arr[i][i]

    return abs(left_right_diagonal - right_left_diagonal)


# print(findMedian([100, 50, 65, 82, 23]))
# print(diagonalDifference(
#     [[1, 2, 6],
#      [2, 78, 4],
#      [234, 4, 5]]))

def countingSort(arr):
    # Write your code here
    resultArr = [0] * 100
    for n in arr:
        resultArr[n] = resultArr[n] + 1
    return resultArr
