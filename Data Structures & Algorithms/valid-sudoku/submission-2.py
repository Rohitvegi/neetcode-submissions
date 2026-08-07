class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                
                if board[i][j] in s:
                    return False
                else:
                    if board[i][j] !='.':
                        s.add(board[i][j])
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                else:
                    if board[j][i] !='.':
                        s.add(board[j][i])
        s=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                n=(i // 3) * 3 + (j // 3)
                if board[i][j] in s[n]:
                    return False
                else:
                    if board[i][j]!='.':
                        s[n].add(board[i][j])
        return True



        