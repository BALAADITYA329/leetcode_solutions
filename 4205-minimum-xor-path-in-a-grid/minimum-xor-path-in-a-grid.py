class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Precompute bit-swapping masks to efficiently shift bitsets under XOR operations
        mask = (1 << 512) - 1
        masks = [0] * 9 + [mask]
        for i in range(8, -1, -1):
            mask ^= mask << (1 << i)
            masks[i] = mask

        def swap(p, v):
            for i in range(10):
                if v & (1 << i):
                    p = ((p & masks[i]) << (1 << i)) | ((p & (masks[i] << (1 << i))) >> (1 << i))
            return p

        # dp[j] stores the bitmask of reachable XOR values for column j
        dp = [0] * n
        
        # Initialize top-left cell
        x = grid[0][0]
        dp[0] = 1 << x
        
        for j in range(1, n):
            x ^= grid[0][j]
            dp[j] = 1 << x
            
        x = grid[0][0]
        for i in range(1, m):
            x ^= grid[i][0]
            dp[0] = 1 << x
            for j in range(1, n):
                # Combine reachable XORs from the left (dp[j-1]) and above (dp[j])
                # and apply XOR with the current grid value
                dp[j] = swap(dp[j - 1] | dp[j], grid[i][j])
                
        # Find the smallest index (XOR value) whose bit is set in the final cell
        return (dp[n - 1] & -dp[n - 1]).bit_length() - 1