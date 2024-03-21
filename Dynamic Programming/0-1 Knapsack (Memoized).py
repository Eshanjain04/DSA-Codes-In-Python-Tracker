wt = [1,3,4,5]
val = [1,4,5,7]
n = 4
w = 7

def knapSackMemoized(wt,val,w,n):
    dp = [[-1 for i in range(w+1)] for j in range(n+1)]
    def helper(wt,val,w,n):
        if n == 0 or w == 0:
            return 0
        if dp[n][w] != -1:
            return dp[n][w]
        if wt[n-1] <= w:
            dp[n][w] =  max(val[n-1]+helper(wt,val,w-wt[n-1],n-1),helper(wt,val,w,n-1))
            return dp[n][w]
        else:
            dp[n][w] = helper(wt,val,w,n-1)
            return dp[n][w]
            
    return helper(wt,val,w,n)
