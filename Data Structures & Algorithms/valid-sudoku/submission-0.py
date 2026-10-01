class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    boxes = [[set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()]]

    for i in range(9):
      for j in range(9):
        # add to col set
        if board[i][j] in cols[j] and board[i][j] != ".":
          return False
        else:
          cols[j].add(board[i][j])
        # add to row set
        if board[i][j] in rows[i] and board[i][j] != ".":
          return False
        else:
          rows[i].add(board[i][j])
        # add to boxes set (i=0,1,2 and j=0,1,2)
        if board[i][j] in boxes[i//3][j//3] and board[i][j] != ".":
          return False
        else:
          boxes[i//3][j//3].add(board[i][j])
    return True      