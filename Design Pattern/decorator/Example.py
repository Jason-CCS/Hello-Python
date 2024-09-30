# Problem 7 - decorator
# Write some examples using python decorator here.

def my_decorator(func):
    def wrapper():
        print("some before() fucntions can be written here.")
        func()
        print("some more after() functions can be written here.")
    return wrapper

@my_decorator
def hello():
    print("Hello Decorator!")


hello()