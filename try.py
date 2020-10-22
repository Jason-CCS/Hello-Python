import sys

while True:
    print('請輸入任意值，如果輸入exit則離開:')
    userInput = str(input())
    if userInput == 'exit':
        print('bye bye')
        sys.exit(1)
    else:
        print('你輸入的是:' + userInput)
