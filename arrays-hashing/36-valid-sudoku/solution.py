from typing import List

class Solution:
    def isValidRow(self, element: str, row: List[str]) -> bool:
        count = 0
        for x in row:
            if x == element:
                count += 1
                if count > 1:
                    return False
        return True

    def isValidColumn(self, element: str, column: List[str]) -> bool:
        count = 0
        for x in column:
            if x == element:
                count += 1
                if count > 1:
                    return False
        return True

    def isValidSquare(self, element: str, square: List[List[str]]) -> bool:
        count = 0
        for r in square:
            for x in r:
                if x == element:
                    count += 1
                    if count > 1:
                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        for i in range(n):
            for j in range(n):
                element = board[i][j]
                if element == ".":
                    continue

                # full row / col
                row = board[i]
                col = [board[r][j] for r in range(n)]

                # 3x3 square for (i, j)
                r0 = (i // 3) * 3
                c0 = (j // 3) * 3
                square = [board[r][c0:c0+3] for r in range(r0, r0+3)]

                if not self.isValidRow(element, row):
                    return False
                if not self.isValidColumn(element, col):
                    return False
                if not self.isValidSquare(element, square):
                    return False

        return True