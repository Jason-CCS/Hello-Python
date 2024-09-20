def palindromeIndex(s):
    # Write your code here
    if isPalindrome(s):
        return -1
    for i in range(len(s)):
        new_list = list(s)
        new_list.pop(i)
        new_s = "".join(new_list)
        if isPalindrome(new_s):
            return i
    return -1


def isPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


print(palindromeIndex("tattarxrattaht"))



