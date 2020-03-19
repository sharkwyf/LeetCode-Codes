class Solution:
    def validTicTacToe(self, board) -> bool:
        def isWin(c: chr) -> bool:
            return any(col.count(c) == 3 for col in board) or \
                any(board[0][i] == board[1][i] == board[2][i] == c for i in range(3)) or \
                all(board[i][i] == c for i in range(3)) or \
                all(board[i][2-i] == c for i in range(3))

        """
        Count O & X in the board
        Check columns
        """
        countO = sum(row.count("O") for row in board)
        countX = sum(row.count("X") for row in board)
        if not countO + 1 >= countX >= countO:
            return False
        if isWin('X') and countX == countO or isWin('O') and countX != countO:
            return False
        return True



a = Solution()
print(a.validTicTacToe(["XXX","OOX","OOX"]))