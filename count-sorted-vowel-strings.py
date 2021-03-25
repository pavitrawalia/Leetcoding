class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0]*5 for i in range(51)]
        
        dp[0] = [1]*5
        
        for i in range(1, n+1):
            temp = 0
            for j in range(4, -1, -1):
                temp += dp[i-1][j]
                dp[i][j] = temp
                
        return(dp[n][0])
