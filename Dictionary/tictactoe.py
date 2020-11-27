gameBoard = {'top-left': ' ', 'top-mid': ' ', 'top-right': ' ',
             'mid-left': ' ', 'mid-mid': ' ', 'mid-right': ' ',
             'bottom-left': ' ', 'bottom-mid': ' ', 'bottom-right': ' '}


def printBoard(board):
    print('{}|{}|{}'.format(board['top-left'], board['top-mid'], board['top-right']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['mid-left'], board['mid-mid'], board['mid-right']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['bottom-left'], board['bottom-mid'], board['bottom-right']))


for i in range(9):
    if i % 2 == 0:
        print('It is O turn. Please enter which position you wanna put: ')
        pos = input()
        gameBoard[pos] = 'O'
    else:
        print('It is X turn. Please enter which position you wanna put: ')
        pos = input()
        gameBoard[pos] = 'X'
    printBoard(gameBoard)
