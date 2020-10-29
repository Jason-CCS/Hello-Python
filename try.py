def dividedBy(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print('您使用的除數是0喔~')


a = int(input('被除數='))
b = int(input('除數='))
print('a/b結果=' + str(dividedBy(a, b)))
