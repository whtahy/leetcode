class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                x = board[row][col]

                if x == '.':
                    continue

                box_row, box_col = row // 3, col // 3

                if x in rows[row] or x in cols[col] or x in boxs[box_row][box_col]:
                    return False

                rows[row].add(x)
                cols[col].add(x)
                boxs[box_row][box_col].add(x)

        return True
