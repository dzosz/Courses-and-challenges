# import time


class Game():

    def __init__(self, themap, cpos, end, **kwargs):
        self.themap = themap
        self.cpos = cpos
        self.end = end
        self.tps = kwargs.setdefault('tps', {})
        self.breaker = False
        self.lastMove = False
        self.moves = [
            ('SOUTH', (1, 0)), ('EAST', (0, 1)),
            ('NORTH', (-1, 0)), ('WEST', (0, -1))]
        self.visited = [0, set()]
        self.path = []

    def validate_move(self, move):
        y, x = (self.cpos[0] + move[0], self.cpos[1] + move[1])
        if self.breaker and self.themap[y][x] == 'X':
            self.themap[y][x] = ' '
        elif self.themap[y][x] in ('X', '#'):
            return False
        return (y, x)

    def teleport(self):
        for tp in self.tps:
            if tp != self.cpos:
                self.cpos = tp
                return True

    def check_field(self):
        y, x = self.cpos
        char = self.themap[y][x]
        if char == 'B':
            self.breaker = False if self.breaker else True
        elif char == 'I':
            self.moves.reverse()
        elif char == 'T':
            self.teleport()
        elif char in ['N', 'S', 'W', 'E']:
            for move in self.moves:
                if move[0].startswith(char):
                    self.lastMove = move
                    return True

    def get_action(self):
        if not (self.lastMove and self.validate_move(self.lastMove[1])):
            for move in self.moves:
                if self.validate_move(move[1]):
                    self.lastMove = move
                    self.cpos = self.validate_move(move[1])
                    return True
        else:
            self.cpos = self.validate_move(self.lastMove[1])
            return True

    def get_path(self):
        while self.cpos != self.end:
            self.check_field()
            self.get_action()
            if self.cpos in self.visited[1]:
                self.visited[0] += 1
            self.visited[1].add(self.cpos)
            self.path.append(self.lastMove[0])
            # print('Turn finished', self.cpos, self.lastMove)
            # time.sleep(0.5)
            if self.visited[0] > 4 * len(self.visited[1]):
                return ['LOOP']
        return self.path

themap = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'I', 'X', 'X', 'X', 'X',
    'X', ' ', '#'], ['#', ' ', ' ', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', 'I', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', 'B', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', 'B', ' ', ' ',
    ' ', 'S', ' ', ' ', ' ', ' ', ' ', 'W', '#'], ['#', ' ', ' ', 'B', ' ',
    ' ', ' ', 'T', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', ' ', ' ', ' ', '#'], ['#', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', '#'], ['#',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X', ' ',
    '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
    '#', '#']]

cpos, end, tps = (2, 3), (12, 13), [(8, 7), (10, 10)]

tomek = Game(themap, cpos, end, tps=tps)

print(*tomek.get_path(), sep = '\n')
