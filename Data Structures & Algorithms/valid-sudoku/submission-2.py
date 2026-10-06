class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getVal(i, j):
            if board[i][j] == ".":
                return None
            else: return (ord(board[i][j]) - ord('0'))
        def checkRows():
            for i in range(9):
                dup = [0] * 9
                for j in range(9):
                    val = getVal(i, j)
                    if not (val is None):
                        if dup[val - 1]:
                            return False
                        dup[val - 1] = 1
            return True
        def checkCols(): 
            for i in range(9):
                dup = [0] * 9
                for j in range(9):
                    val = getVal(j, i)
                    if not (val is None):
                        if dup[val - 1]:
                            return False
                        dup[val - 1] = 1
            return True
        def checkBoxes():
            for i in range(3):
                for j in range(3):
                    dup = [0] * 9
                    for k in range(i * 3, (i + 1) * 3):
                        for l in range(j * 3, (j + 1) * 3):
                            val = getVal(k, l)
                            if not(val is None):
                                if dup[val - 1]:
                                    return False
                                dup[val - 1] = 1
            return True
        return checkRows() and checkCols() and checkBoxes()
                 

