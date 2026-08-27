class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            y= set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in y:
                    return False
    
                y.add(board[row][i])        
                    
        for col in range(9):
            y= set()
            for i in range(9):
                if board[i][col] == ".": 
                    continue
                if board[i][col] in y:
                    return False

                y.add(board[i][col])   

        for box in range(9):
            y= set()
            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i
                    col = (box % 3) * 3 + j
                    if board[row][col] == ".": 
                      continue
                    if board[row][col] in y:
                        return False
                
                    y.add(board[row][col])                                    

                        
        return True                    
    