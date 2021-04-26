class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toString(self):
        return 'name: {}, age: {}'.format(self.name, self.age)


p1 = Person('Jason', 35)
print(p1.toString())
