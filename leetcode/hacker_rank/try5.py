def superDigit(n, k):
    # Write your code here
    if len(n) == 1 and k == 1:
        return int(n)
    else:
        sum = 0
        for c in n:
            sum += int(c)
        sum = sum * k
        if len(str(sum)) > 1:
            return superDigit(str(sum), 1)
        else:
            return int(sum)


print(superDigit("9875", 4))
