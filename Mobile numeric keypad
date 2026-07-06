There is a standard numeric keypad on a mobile phone. You can press the current button or any button that is directly above, below, to the left, or to the right of it. For example, if you press 5, then pressing 2, 4, 6, or 8 is allowed. However, diagonal movements and pressing the bottom row corner buttons (* and #) are not allowed.
Given an integer n, determine how many unique sequences of length n can be formed by pressing buttons on the keypad, starting from any digit.

class Solution:
    def getCount(self, n):
        if n == 1:
            return 10

        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [1, 2, 3, 5],
            3: [2, 3, 6],
            4: [1, 4, 5, 7],
            5: [2, 4, 5, 6, 8],
            6: [3, 5, 6, 9],
            7: [4, 7, 8],
            8: [5, 7, 8, 9, 0],
            9: [6, 8, 9]
        }

        dp = [1] * 10

        for _ in range(2, n + 1):
            new = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    new[i] += dp[j]
            dp = new

        return sum(dp)
