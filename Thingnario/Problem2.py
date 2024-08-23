# Problem 2 - Find second largest
def find_second_largest(sequence):
    # Write your algorithm with O(n) time complexity here.
    if len(sequence) < 2:
        return None

    # real implementation starts from here
    largest, second_largest = float('-inf'), float('-inf')
    for i in sequence:
        if i > largest:
            largest = i
        elif largest > i > second_largest:
            second_largest = i

    # if second_largest is '-inf', return None for better comprehension.
    if second_largest == float('-inf'):
        return None

    return second_largest


print(find_second_largest([3, 3, 3, 3]))
print(find_second_largest([3, 3, 3, 3, 3, 2, 2, 1]))
print(find_second_largest([-1, 2, 3, 5, 3, 1, 2, 4]))
assert find_second_largest([3, 3, 2, 1]) == 2
assert find_second_largest([3, 3, 3, 3, 3, 2, 2, 1]) == 2
assert find_second_largest([-1, 2, 3, 5, 3, 1, 2, 4]) == 4
