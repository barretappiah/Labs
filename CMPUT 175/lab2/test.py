SIZE = 3

class TicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = SIZE   # number of columns and rows of board
        
        # populate the empty squares in board with " "
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.board.append(row)
    
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
        
        print('   1   2   3 ')
        seperator = '  -----------'
        for x in range(len(self.board)):
            temp = []
            for y in self.board[x]:
                if y == " ":
                    temp.append("   ")
                elif y == "O": 
                    temp.append(' \033[91mO\033[0m ')
                elif y == "X":
                    temp.append(' \033[95mX\033[0m ') 
                else:
                    temp.append(str(y))
            print(f'{x+1} {"|".join(temp)}')
            if x != len(self.board) - 1: 
                print(seperator)

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a symbol.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] == " ":
            return True
        elif self.board[row][col] != " ":
            return False
        
    def update(self, row, col, letter):
        '''
        Assigns the letter, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           letter (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col) == True: 
            self.board[row][col] = letter       
            return True
        elif self.squareIsEmpty(row,col) == False:
            return False

myBoard = TicTacToe()
print(myBoard.update(1,1,'X'))
myBoard.update(1,1,'X')
print(myBoard.update(1,1,'X'))
myBoard.drawBoard()