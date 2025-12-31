class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        # dp_prev[j][r] = number of ways to reach previous row, column j with remainder r
        dp_prev = []
        for j in range(n):
            remainders = [0] * k
            dp_prev.append(remainders)

        # dp_curr[j][r] = for the current row
        dp_curr = []
        for j in range(n):
            remainders = [0] * k
            dp_curr.append(remainders)

        # Fill first cell (0,0)
        first_rem = grid[0][0] % k
        dp_prev[0][first_rem] = 1

        # Fill first row separately
        for j in range(1, n):
            val = grid[0][j] % k
            for r in range(k):
                if dp_prev[j-1][r] > 0:
                    new_r = (r + val) % k
                    dp_prev[j][new_r] += dp_prev[j-1][r]
                    dp_prev[j][new_r] %= MOD

        # Process remaining rows
        for i in range(1, m):

            # Reset dp_curr for the new row
            for j in range(n):
                for r in range(k):
                    dp_curr[j][r] = 0

            for j in range(n):
                val = grid[i][j] % k

                for r in range(k):

                    # From top (previous row)
                    if dp_prev[j][r] > 0:
                        new_r = (r + val) % k
                        dp_curr[j][new_r] += dp_prev[j][r]

                    # From left (current row)
                    if j > 0 and dp_curr[j-1][r] > 0:
                        new_r = (r + val) % k
                        dp_curr[j][new_r] += dp_curr[j-1][r]

                # Mod
                for r in range(k):
                    dp_curr[j][r] %= MOD

            # Move dp_curr → dp_prev
            for j in range(n):
                for r in range(k):
                    dp_prev[j][r] = dp_curr[j][r]

        # Answer: remainder 0 at bottom-right
        return dp_prev[n-1][0]

        
