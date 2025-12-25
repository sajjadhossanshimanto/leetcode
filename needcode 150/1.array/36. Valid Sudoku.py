#%%
from typing import List


empty_cell = "."
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checks row
        for r in board:
            seen = set()
            for i in r:
                if i!=empty_cell and i in seen: 
                    return False
                seen.add(i)
        
        # checks column
        for c in range(9):
            seen = set()
            for r in board:
                if r[c]!=empty_cell and r[c] in seen: 
                    return False
                seen.add(r[c])
        
        # checks cell
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        # print(i, j)
                        # print(board[r][c+i])
                        ele = board[i][j]

                        if ele!=empty_cell and ele in seen: 
                            return False
                        seen.add(ele)
                # print("------------")
        return True

#%%
s = Solution()
s.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
# %%
