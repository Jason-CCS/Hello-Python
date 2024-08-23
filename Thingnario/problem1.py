# Problem 1 - Bubble sort
def bubble_sort(sequence):
    # write your bubble sort code here.
    for i in range(len(sequence) - 1):
        for j in range(len(sequence) - 1 - i):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]

    return sequence


assert bubble_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]
print(bubble_sort([5, 1, 3, 2, 4]))
