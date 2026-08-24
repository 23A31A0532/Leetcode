class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate prefix sums and prepare to handle these in backward order
        prf = [*accumulate(stones)][1:][::-1]
        
        # Now, dp[0]=prf[0] and dp[i] = max(dp[i-1], prf[i]-dp[i-1])
        return  reduce(lambda s,e: max(s,e-s), prf[1:], initial=prf[0])
        