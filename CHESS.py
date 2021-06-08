from tkinter import *
from keyboard import is_pressed as pressed

tk = Tk()
tk.overrideredirect(True)
canvas = Canvas(tk, bg = 'black', width = 600, height = 600)
canvas.pack()

class Piece:
    def __init__(self, x, y, team, esc):
        self.x = x
        self.y = y
        self.team = team
        self.esc = esc
        self.moved = False
        self.piece = True
        self.oposite = 'white' if self.team == 'black' else 'black'

class Pawn(Piece):
    def __init__(self, x, y, team, esc):
        super().__init__(x, y, team, esc)
        self.dir = 1 if team == 'white' else -1
    
    def future(self, board):
        moves = []
        foe = 'white' if self.team == 'black' else 'black'
        if self.y + self.dir in range(8): 
            piece = board[self.y + self.dir][self.x]
            try:
                if piece.piece: pass
            except AttributeError:
                moves += [[self.x, self.y + self.dir]]
                if self.moved == False:
                    try:
                        if board[self.y + self.dir * 2][self.x].piece: pass
                    except AttributeError:
                        moves += [[self.x, self.y + self.dir * 2]]

        if self.y + self.dir in range(8):
            if self.x - 1 in range(8):
                piece = board[self.y + self.dir][self.x - 1]
                try:
                    if piece.team == foe:
                        moves += [[self.x - 1, self.y + self.dir]]
                except AttributeError: pass
            if self.x + 1 in range(8):
                piece = board[self.y + self.dir][self.x + 1]
                try:
                    if piece.team == foe:
                        moves += [[self.x + 1, self.y + self.dir]]
                except AttributeError: pass
        return moves
    
    def show(self):
        offset = self.esc * .5
        x = self.x * self.esc + offset
        y = self.y * self.esc + offset
        r = self.esc  * .4
        canvas.create_oval(x - r, y - r, x + r, y + r, fill = self.team, outline = self.oposite, width = 3)

class Knight(Piece):
    def __init__(self, x, y, team, esc):
        super().__init__(x, y, team, esc)
    
    def show(self):
        offset = self.esc * .5
        x, y = self.x * self.esc + offset, self.y * self.esc + offset
        r = self.esc * .4
        points = [
            x - r + 5, y + r, x + r, y + r, x + r, y - r - 5,
            x + r - 5, y - r, x + r - 10, y - r - 5, x - r * .5, y - r - 5,
            x - r * .5, y, x, y, x - r + 5, y + r
        ]
        canvas.create_polygon(points, fill = self.team, outline = self.oposite, width = 3)
    
    def future(self, board):
        directions = [
            (-1, -2),
            (-2, -1),
            (-2, 1),
            (-1, 2),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2)
        ]
        moves = []
        foe = 'white' if self.team == 'black' else 'black'
        for d in directions:
            dx = self.x + d[0]
            dy = self.y + d[1]
            if dx in range(8):
                if dy in range(8):
                    try:
                        if board[dy][dx].team == foe:
                            moves += [[dx, dy]]
                        else: pass
                    except AttributeError:
                        moves += [[dx, dy]]
        return moves

class Bishop(Piece):
    def __init__(self, x, y, team, esc):
        super().__init__(x, y, team, esc)

    def show(self):
        offset = self.esc * .5
        x, y = self.x * self.esc + offset, self.y * self.esc + offset
        r = self.esc * .4
        canvas.create_polygon(x - r, y + r, x + r, y + r, x, y - r, fill = self.team, outline = self.oposite, width = 3)
    
    def future(self, board):
        x, y = self.x, self.y
        moves = []
        for _y in (-1, 1):
            for _x in (-1, 1):
                for n in range(1, 8):
                    if x + n * _x in range(8):
                        if y + n * _y in range(8):
                            piece = board[y + n * _y][x + n * _x]
                            try:
                                if piece.team == self.oposite:
                                    moves += [[x + n * _x, y + n * _y]]
                                    break
                                elif piece.team == self.team:
                                    break
                            except AttributeError:
                                moves += [[x + n * _x, y + n * _y]]
        return moves

class Tower(Piece):
    def __init__(self, x, y, team, esc):
        super().__init__(x, y, team, esc)

    def show(self):
        offset = self.esc * .5
        x, y = self.x * self.esc + offset, self.y * self.esc + offset
        r = self.esc * .4
        h = 20
        points = [
            x - r, y - r, 
            x + r, y - r,
            x + r, y - r + h,
            x + r * .5, y - r + h,
            x + r * .5, y + r,
            x - r * .5, y + r,
            x - r * .5, y - r + h,
            x - r, y - r + h,
            x - r, y - r
        ]
        canvas.create_polygon(points, fill = self.team, outline = self.oposite, width = 3)

    def future(self, board):
        x, y = self.x, self.y
        moves = []
        for _y in (-1, 1):
            for n in range(1, 8):
                if y + n * _y in range(8):
                    piece = board[y + n * _y][x]
                    try:
                        if piece.team == self.oposite:
                            moves += [[x, y + n * _y]]
                            break
                        elif piece.team == self.team:
                            break
                    except AttributeError:
                        moves += [[x, y + n * _y]]
        for _y in (-1, 1):
            for n in range(1, 8):
                if x + n * _y in range(8):
                    piece = board[y][x + n * _y]
                    try:
                        if piece.team == self.oposite:
                            moves += [[x + n * _y, y]]
                            break
                        elif piece.team == self.team:
                            break
                    except AttributeError:
                        moves += [[x + n * _y, y]]
        return moves

class Queen(Piece):
    def __init__(self, x, y, team, esc):
        super().__init__(x, y, team, esc)

    def show(self):
        offset = self.esc * .5
        q = self.esc * .25
        r = self.esc * .4
        h = 10
        x, y = self.x * self.esc + offset, self.y * self.esc + offset + h
        canvas.create_rectangle(x - r, y - h, x + r, y + h, fill = self.team, outline = self.oposite, width = 3)
        for p in range(1, 4):
            r = self.esc / 8
            ox = q * p + self.x * self.esc
            oy = y - h - r
            canvas.create_oval(ox - r, oy - r, ox + r, oy + r, fill = self.team, outline = self.oposite, width = 3)

    def future(self, board):
        x, y = self.x, self.y
        moves = []
        for _y in (-1, 1):
            for _x in (-1, 1):
                for n in range(1, 8):
                    if x + n * _x in range(8):
                        if y + n * _y in range(8):
                            piece = board[y + n * _y][x + n * _x]
                            try:
                                if piece.team == self.oposite:
                                    moves += [[x + n * _x, y + n * _y]]
                                    break
                                elif piece.team == self.team:
                                    break
                            except AttributeError:
                                moves += [[x + n * _x, y + n * _y]]
        for _y in (-1, 1):
            for n in range(1, 8):
                if y + n * _y in range(8):
                    piece = board[y + n * _y][x]
                    try:
                        if piece.team == self.oposite:
                            moves += [[x, y + n * _y]]
                            break
                        elif piece.team == self.team:
                            break
                    except AttributeError:
                        moves += [[x, y + n * _y]]
        for _y in (-1, 1):
            for n in range(1, 8):
                if x + n * _y in range(8):
                    piece = board[y][x + n * _y]
                    try:
                        if piece.team == self.oposite:
                            moves += [[x + n * _y, y]]
                            break
                        elif piece.team == self.team:
                            break
                    except AttributeError:
                        moves += [[x + n * _y, y]]
        return moves

class King(Piece):
    def __init__(self, x, y, team, esc):
        super().__init__(x, y, team, esc)
    
    def show(self):
        offset = self.esc * .5
        r = self.esc * .4
        w = 10
        x, y = self.x * self.esc + offset, self.y * self.esc + offset
        points = [
            x + r, y + w,
            x + r, y - w,
            x + w, y - w,
            x + w, y - r,
            x - w, y - r,
            x - w, y - w,
            x - r, y - w,
            x - r, y + w,
            x - w, y + w,
            x - w, y + r,
            x + w, y + r,
            x + w, y + w
        ]
        canvas.create_polygon(points, fill = self.team, outline = self.oposite, width = 3)

    def future(self, board):
        x, y = self.x, self.y
        moves = []
        for _y in (-1, 0, 1):
            for _x in (-1, 0, 1):
                for n in range(1, 2):
                    if x + n * _x in range(8):
                        if y + n * _y in range(8):
                            piece = board[y + n * _y][x + n * _x]
                            try:
                                if piece.team == self.oposite:
                                    moves += [[x + n * _x, y + n * _y]]
                                    break
                                elif piece.team == self.team:
                                    break
                            except AttributeError:
                                moves += [[x + n * _x, y + n * _y]]
        return moves
        
class Board:
    def __init__(self, esc):
        self.esc = esc
        self.board = self.reset()
        self.moves = self.reset()
        self.base = self.reset()
        self.pieces = [
            [0 for _ in range(8)],
            [Pawn(x, 1, 'white', self.esc) for x in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [Pawn(x, 6, 'black', self.esc) for x in range(8)],
            [0 for _ in range(8)]
        ]
        # self.pieces = [[0 for _ in range(8)] for _ in range(8)]
        self.pieces[0][0] = Tower(0, 0, 'white', self.esc)
        self.pieces[0][7] = Tower(7, 0, 'white', self.esc)
        self.pieces[7][0] = Tower(0, 7, 'black', self.esc)
        self.pieces[7][7] = Tower(7, 7, 'black', self.esc)

        self.pieces[0][1] = Knight(1, 0, 'white', self.esc)
        self.pieces[0][6] = Knight(6, 0, 'white', self.esc)
        self.pieces[7][6] = Knight(6, 7, 'black', self.esc)
        self.pieces[7][1] = Knight(1, 7, 'black', self.esc)

        self.pieces[0][2] = Bishop(2, 0, 'white', self.esc)
        self.pieces[0][5] = Bishop(5, 0, 'white', self.esc)
        self.pieces[7][2] = Bishop(2, 7, 'black', self.esc)
        self.pieces[7][5] = Bishop(5, 7, 'black', self.esc)

        self.pieces[0][3] = Queen(3, 0, 'white', self.esc)
        self.pieces[0][4] = King(4, 0, 'white', self.esc)
        self.pieces[7][3] = Queen(3, 7, 'black', self.esc)
        self.pieces[7][4] = King(4, 7, 'black', self.esc)

        self.sel = [0, 0]   
        self.white_king = self.pieces[0][4]
        self.black_king = self.pieces[7][4]
        self.turn = 'black'
        self.choice = False
        self.possible = 0
        self.choose = 0

    def reset(self):
        b = []
        for y in range(8):
            index = y
            aux = []
            for x in range(8):
                color = 'white' if index % 2 == 0 else 'black'
                aux += [color]
                index += 1
            b += [aux]
        return b

    def show_pieces(self):
        for row in self.pieces:
            for piece in row:
                try: piece.show()
                except AttributeError: pass

    def show(self):
        esc = self.esc
        for y in range(8):
            for x in range(8):
                color = self.base[y][x]
                move = self.moves[y][x]
                select = self.board[y][x]
                canvas.create_rectangle(x * esc, y * esc, x * esc + esc, y * esc + esc, fill = color)
                if move != color: canvas.create_rectangle(x * esc, y * esc, x * esc + esc, y * esc + esc, fill = move)
                if select != color: canvas.create_rectangle(x * esc, y * esc, x * esc + esc, y * esc + esc, fill = select)
    
    def select(self, x, y):
        if self.sel[0] + x in range(8):
            if self.sel[1] + y in range(8):
                    self.board = self.reset()
                    self.sel[0] += x
                    self.sel[1] += y
                    self.board[self.sel[1]][self.sel[0]] = 'grey'

    def check_mate(self):
        if self.turn == 'white':
            king = [self.black_king.x, self.black_king.y]
        else:
            king = [self.white_king.x, self.white_king.y]
        for row in self.pieces:
            for piece in row:
                try:
                    if piece.team == self.turn:
                        moves = piece.future(self.pieces)
                        if king in moves:
                            print(self.team, 'mate')
                            self.board[king[1]][king[0]] = 'red'
                except AttributeError: pass

    def future(self):
        if self.choice == False:
            piece = self.pieces[self.sel[1]][self.sel[0]]
            try:
                if piece.oposite == self.turn:
                    moves = piece.future(self.pieces)
                    for move in moves:
                        self.moves[move[1]][move[0]] = 'red'
                    self.choice = True
                    self.possible = moves
                    self.choose = piece
            except AttributeError: pass
        else: 
            self.moves = self.reset()
            self.choice = False
            if self.sel in self.possible:
                prevx, prevy = self.choose.x, self.choose.y
                x, y = self.sel
                new = self.pieces[y][x]
                self.choose.moved = True
                try:
                    if self.choose.piece: self.pieces[y][x] = 0
                except AttributeError: pass    
                self.choose.x = x
                self.choose.y = y
                self.pieces[prevy][prevx], self.pieces[y][x] = 0, self.choose
                self.turn = 'white' if self.turn == 'black' else 'black'

def key(k):
    if pressed(k):
        while pressed(k):
            pass
        return True
    return False

def refresh():
    canvas.delete(ALL)
    board.check_mate()
    board.show()
    board.show_pieces()

board = Board(75)
refresh()
while True:
    if key('left'): 
        board.select(-1, 0)
        refresh()
    if key('right'): 
        board.select(1, 0)
        refresh()
    if key('up'): 
        board.select(0, -1)
        refresh()
    if key('down'): 
        board.select(0, 1)
        refresh()
    if key(' '): 
        board.check_mate()
        board.future()
        refresh()
    tk.update()

tk.mainloop()
