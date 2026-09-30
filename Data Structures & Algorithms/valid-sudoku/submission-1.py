class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for col in range(9):
            colSeen = set()
            
            for i in range(9):
                print(board[i][col],i)
                if board[i][col] == ".":
                    continue
                if board[i][col] in colSeen:
                    
                    return False
                
                colSeen.add(board[i][col])
        
        for row in range(9):
            rowSeen = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in rowSeen:
                    
                    return False
                rowSeen.add(board[row][j])
            
        for i in range(9):
            sqr = set()
           
            for x in range(3):
                for y in range(3):
                    newX = x + ((i//3)*3)
                    newY = y + ((i%3) * 3)
                   
                    if board[newX][newY] == ".":
                        continue
                    if board[newX][newY] in sqr:
                        return False
                    sqr.add(board[newX][newY])
        return True

