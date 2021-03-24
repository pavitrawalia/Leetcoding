class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n=cost.size();
        vector dp(n,INT_MAX);
        
        dp[0]=0;
        dp[1]=min(cost[0],cost[1]);
        
        for(int i=2;i<n;i++){
        dp[i]=min(cost[i]+dp[i-1],cost[i-1]+dp[i-2]);
        }
        
        return dp[n-1];
    }
};
