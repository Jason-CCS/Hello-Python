# Problem 6 - comprehension
# Write some examples using python comprehension here.

squares = [x**2 for x in range(10)]
unique_squares = {x**2 for x in range(10)}
square_dict = {x: x**2 for x in range(10)}

print(squares)
print(unique_squares)
print(square_dict)