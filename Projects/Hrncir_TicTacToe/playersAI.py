import random as rd

EMPTYSYM = ''
DIRECTIONS = [[-1, 0], [-1, 1], [0, 1],
              [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


class Player:
    def __init__(self, my_sym, opp_sym):
        self.my_sym = my_sym
        self.opp_sym = opp_sym

    def move(self, board):
        moves = self.find_possible_move(board)
        return rd.choice(moves)

    def find_possible_move(self, board):
        moves = []
        for i, row in enumerate(board):
            for j, place in enumerate(row):
                if place == EMPTYSYM:
                    moves.append((i, j))
        return moves


class PlayerBlocker(Player):
    def is_on_board(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def maximalize_length(self, startPos, max_sym, board):
        for pos in startPos:
            x = pos[0]
            y = pos[1]
            for dir in DIRECTIONS:
                xDir = x + dir[0]
                yDir = y + dir[1]
                len = 0
                while self.is_on_board(xDir, yDir) and board[xDir][yDir] == max_sym:
                    len += 1
                    xDir = xDir + dir[0]
                    yDir = yDir + dir[1]
                if len == 2:
                    return pos

    def move(self, board):
        moves = self.find_possible_move(board)
        blockMove = self.maximalize_length(moves, self.opp_sym, board)
        if blockMove != None:
            return blockMove
        else:
            return moves[0]


class PlayerMax(PlayerBlocker):
    def move(self, board):
        moves = self.find_possible_move(board)
        winMove = self.maximalize_length(moves, self.my_sym, board)
        if winMove != None:
            return winMove
        else:
            return moves[0]


if __name__ == "__main__":
    p1 = Player('X', 'O')
    pB = PlayerBlocker('O', 'X')
    pM = PlayerMax('X', 'O')
    board1 = [['X', '', 'X'], ['d', 's', ''], ['', 's', '']]
    board2 = [['X', '', 'X'],
              ['d', 'X', ''],
              ['', 's', '']]
    board3 = [['X', 'd', 'X'],
              ['d', 'X', ''],
              ['d', 's', '']]
    print(p1.move(board1))

    print(pB.move(board3))

    print(pM.move(board2))
