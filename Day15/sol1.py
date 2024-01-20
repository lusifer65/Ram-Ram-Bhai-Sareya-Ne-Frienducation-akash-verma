class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
            Do not return anything, modify board in-place instead.
        """

        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.' 
                        return False  
            return True  

        solve(board)
