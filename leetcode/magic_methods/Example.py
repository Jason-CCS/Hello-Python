# Problem 10 - magic methods
# Write some examples using python magic methods here.
class Word():
    def __init__(self, text):
        self.text = text

    # comare equity, ignoring case
    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    # like Java toString()
    def __str__(self):
        return self.text

    # a verbose toString()
    def __repr__(self):
        return f"Word(text={self.text})"

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)
print(first)
print(repr(first))