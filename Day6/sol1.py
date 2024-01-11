class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                current_val = board[i][j]
                if current_val != '.':
                    # Check for row uniqueness
                    if (i, current_val) in seen:
                        return False
                    seen.add((i, current_val))

                    # Check for column uniqueness
                    if (current_val, j) in seen:
                        return False
                    seen.add((current_val, j))

                    # Check for box uniqueness
                    if (i // 3, j // 3, current_val) in seen:
                        return False
                    seen.add((i // 3, j // 3, current_val))

        return True
