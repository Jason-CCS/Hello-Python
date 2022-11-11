def bold(func):
    def inner():
        return "<b>" + func() + "</b>"

    return inner


@bold
def hey():
    return "hey"

print(hey())