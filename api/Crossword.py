GRID_SIZE = 15

class Crossword():
    def __init__(self, board=None, across_clues={}, down_clues={}):
        if board != None:
            self.board = board
        else:
            self.board = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.across_clues = across_clues
        self.down_clues = down_clues

    '''
    Generates a new crossword puzzle using a list of words
    '''
    def create_crossword(self, words):
        return None
    
    '''
    Checks a user board compared to the actual board
    Returns True or false depending on the correct letters and returns a board of incorrect  
    '''
    def check_crossword(self, user_board):
        correct_board = [[True for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        isCorrect = True
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] != user_board[i][j]:
                    correct_board[i][j] = False
                    isCorrect = False
        return isCorrect, correct_board
    
    '''
    Creates a board to show where user input should be without revealing answers to frontend
    0 for input spot and . for black spot
    '''
    def create_mask_board(self):
        return [["." if x == "." else "0" for x in row] for row in self.board]

