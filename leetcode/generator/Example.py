# Problem 8 - generator
# Write some examples using python generator here.

square_gen = (x**2 for x in range(10))
for e in square_gen:
    print(e)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):
    print(next(fib))

# Explain the benefit of generators here.
# 1. lazy initialization to save memory, especially when we want to initialize a big dataset.
# 2. I have checked some explanations from internet.
#    It's like Java's Iterator. Calculate the result when you call the next().
#    Therefore, it saves the memory and processing time if you compare with
#    calculating all the value in a list, and get the result from it one by one.