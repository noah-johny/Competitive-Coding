from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value != ".":
                    if (value in rows[row] or value in cols[col] or value in squares[(row // 3, col // 3)]):
                        return False
                    else:
                        rows[row].add(value)
                        cols[col].add(value)
                        squares[(row // 3, col // 3)].add(value)
        return True