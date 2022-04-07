class Solution(object):
   def isValidSudoku(self, board):
      """
      :type board: List[List[str]]
      :rtype: bool
      """
      for i in range(9):
         row = {}
         column = {}
         block = {}
         row_cube = 3 * (i//3)
         column_cube = 3 * (i%3)
         for j in range(9):
            if board[i][j]!='.' and board[i][j] in row:
               return False
            row[board[i][j]] = 1
            if board[j][i]!='.' and board[j][i] in column:
               return False
            column[board[j][i]] = 1
            rc= row_cube+j//3
            cc = column_cube + j%3
            if board[rc][cc] in block and board[rc][cc]!='.':
               return False
            block[board[rc][cc]]=1
      return True


def check_sudoku(grid):
   """ Return True if grid is a valid Sudoku square, otherwise False. """
   for i in range(9):
      # j, k index top left hand corner of each 3x3 tile
      j, k = (i // 3) * 3, (i % 3) * 3
      if len(set(grid[i, :])) != 9 or len(set(grid[:, i])) != 9 \
              or len(set(grid[j:j + 3, k:k + 3].ravel())) != 9:
         return False
   return True


sudoku = """145327698
            839654127
            672918543
            496185372
            218473956
            753296481
            367542819
            984761235
            521839764"""
# Turn the provided string, sudoku, into an integer array
grid = np.array([[int(i) for i in line] for line in sudoku.split()])
print(grid)

if check_sudoku(grid):
   print('grid valid')
else:
   print('grid invalid')