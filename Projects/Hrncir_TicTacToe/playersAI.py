import random as rd
from copy import deepcopy


WINSIZE = 3
EMPTYSYM = ''
DIRECTIONS = [[-1, 0], [-1, 1], [0, 1],
              [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


class Player:
    def __init__(self, my_symbol, opp_symbol):
        self.my_symbol = my_symbol
        self.opp_symbol = opp_symbol

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
        blockMove = self.maximalize_length(moves, self.opp_symbol, board)
        if blockMove != None:
            return blockMove
        else:
            return moves[0]


class PlayerMax(PlayerBlocker):
    def move(self, board):
        moves = self.find_possible_move(board)
        winMove = self.maximalize_length(moves, self.my_symbol, board)
        if winMove != None:
            return winMove
        else:
            return moves[0]


class PlayerMinimax(Player):
    def list_check(self, board):
        for row in board:
            count = 0
            firstVal = row[0]
            for val in row:
                if firstVal == val and val != EMPTYSYM:
                    count += 1
            if count == WINSIZE:
                return True
        return False

    def win_check(self, board):
        # horizontal
        if self.list_check(board):
            return True
        # vertial
        column = []
        col0 = []
        col2 = []
        col1 = []
        for row in board:
            col0.append(row[0])
            col1.append(row[1])
            col2.append(row[2])
        column.append(col0)
        column.append(col1)
        column.append(col2)
        if self.list_check(column):
            return True
        # diagonal
        if board[0][0] == board[1][1] == board[2][2] != EMPTYSYM:
            return True
        elif board[0][2] == board[1][1] == board[2][0] != EMPTYSYM:
            return True
        else:
            return False

    def is_draw(self, board):
        count = 0
        for r in board:
            for v in r:
                if v != EMPTYSYM:
                    count += 1
        if count == 9:
            return True
        else:
            return False

    def simulate_move(self, board, move, m_sym):
        board[move[0]][move[1]] = m_sym
        return board

    def evaluate(self, player):
        if player == self.my_symbol:
            return -10
        elif player == self.opp_symbol:
            return 10

    def minimax(self, board, player):
        if self.win_check(board):
            return (self.evaluate(player), None)
        elif self.is_draw(board):
            return (0, None)
        moves = self.find_possible_move(board)
        # max player
        if player == self.my_symbol:
            m_sym = player
            opp_sym = self.opp_symbol
            max_move = None
            max_score = -100  # negative infinity
            for move in moves:
                new_board = deepcopy(board)
                new_board = self.simulate_move(new_board, move, m_sym)
                eval = self.minimax(new_board, opp_sym)
                if eval[0] > max_score:
                    max_score = eval[0]
                    max_move = move
            return (max_score, max_move)
        # min player
        elif player == self.opp_symbol:
            m_sym = player
            opp_sym = self.my_symbol
            min_move = None
            min_score = 100  # infinity
            for move in moves:
                new_board = deepcopy(board)
                new_board = self.simulate_move(new_board, move, m_sym)
                eval = self.minimax(new_board, opp_sym)
                if eval[0] < min_score:
                    min_score = eval[0]
                    min_move = move
            return (min_score, min_move)

    def move(self, board):
        return self.minimax(board, self.my_symbol)[1]


if __name__ == "__main__":
    p1 = Player('X', 'O')
    pB = PlayerBlocker('O', 'X')
    pM = PlayerMax('X', 'O')
    pMinimax = PlayerMinimax('X', 'O')
    board1 = [['X', 'd', 'X'], ['d', 'X', 'd'], ['d', 's', 'X']]
    board2 = [['X', '', 'X'],
              ['d', 'X', ''],
              ['', 's', '']]
    board3 = [['X', 'd', 'X'],
              ['d', 'X', ''],
              ['d', 's', '']]
    board4 = [['X', 'O', 'X'],
              ['', '', ''],
              ['O', 'O', 'X']]
    board5 = [['O', '', 'X'],
              ['X', '', ''],
              ['X', 'O', 'O']]
    board6 = [['X', 'O', 'X'],
              ['O', 'O', 'X'],
              ['', '', '']]
    # print(p1.move(board1))

    # print(pB.move(board3))

    # print(pM.move(board2))

    print(pMinimax.win_check(board1))
    print(pMinimax.is_draw(board1))
    print(pMinimax.move(board2))
    print(pMinimax.move(board4))
    print(pMinimax.move(board5))
    print(pMinimax.move(board6))
