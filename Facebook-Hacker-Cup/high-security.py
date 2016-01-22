"""
Facebook Hacker Cup 2016 Qualification Round

STRATEGY:

    - start with top row, place guards only on rows where free
      space is more than 1 and in places where bottom space is
      single
    - then add guards to all voids in second row that are
      sperated by wall 'X'
    - the program fills array with letters 'G' for guards visibility

To debug change logging level to 20.
"""

import logging
logging.basicConfig(level=30, format="%(message)s")


def isalone(y, x):
    return (x == 0 or board[y][x-1] == 'X') and board[y][x+1] == 'X'


def setguard(y, x):
    logging.info('setting for %s %s', y, x)

    # set middle position if possible
    board[0][x] = 'G' if board[1][x] == '.' else 'X'
    board[1][x] = 'G' if board[1][x] == '.' else 'X'

    # from middle to the left
    for i in range(x-1, -1, -1):
        if board[y][i] == 'X':
            break
        else:
            board[y][i] = 'G'

    # from middle to the right
    for j in range(x+1, size):
        if board[y][j] == 'X':
            break
        else:
            board[y][j] = 'G'


games = int(input())

for game in range(games):
    size = int(input())
    board = list(map(list, [input(), input()]))

    # add walls to the end to avoid exceptions
    board[0].extend('X')
    board[1].extend('X')

    counter = 0
    guards = 0

    for i in range(size+1):
        a = board[0][i]
        b = board[1][i]

        if a  == '.':
            counter += 1
            if b == '.' and isalone(1, i):
                guards += 1
                setguard(0, i)
                counter = 0
        elif a == 'G':
            pass
        else:
            # encountered wall on the first row
            if counter == 1:
                if board[1][i-1] != 'X':
                    setguard(1, i-1)
                else:
                    setguard(0, i-1)
                guards += 1
            elif counter > 1:
                setguard(0, i-1)
                guards += 1
            counter = 0

    # Filling gaps in second row
    counter = 0

    for j in range(size+1):
        b = board[1][j]
        if b  == '.':
            counter += 1
        elif b == 'G':
            pass
        else:
            if counter > 0:
                setguard(1, j-1)
                guards += 1
                counter = 0


    logging.info("%s\n%s", *board)
    print("Case #{}: {}".format(game+1, guards))
    logging.info('-'*40)
