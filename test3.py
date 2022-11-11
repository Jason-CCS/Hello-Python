class KeyNotFoundError(BaseException):
    pass


class Keyboard:
    def input_letter(self):
        print('letter')

    def input_fn(self):
        print('fn')

    def input_arrow(self):
        print('arrow')

    def input_number(self):
        print('number')


class SixtyPercentKeyboard(Keyboard):
    # def __init__(self):
    def input_letter(self):
        print('letter')

    def input_fn(self):
        raise KeyNotFoundError

    def input_arrow(self):
        raise KeyNotFoundError

    def input_number(self):
        raise KeyNotFoundError


class EightyPercentKeyboard(SixtyPercentKeyboard):
    def input_fn(self):
        print('fn')

    def input_arrow(self):
        print('arrow')


class FullKeyboard(EightyPercentKeyboard):
    def input_number(self):
        print('number')
