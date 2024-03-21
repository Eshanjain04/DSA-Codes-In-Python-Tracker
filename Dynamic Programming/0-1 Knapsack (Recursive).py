# Let's say you have a knapsack with a constraint weight and a list of objects given with weights and values associated with it.
# You have to store these weights in your knapsack to get the maximum value
# e.g wt = [1,3,4,5]
# val = [1,4,5,7]
# n = 4
# w = 7
# We will recursively check if the weight can be stored in our bag if by adding it, the weight is less than the constraint weight


def knapSackRecursive(wt,val,w,n):
    def helper(wt,val,w,n):
        if n == 0 or w == 0:
            return 0
        if wt[n-1] <= w:
            return max(val[n-1]+helper(wt,val,w-wt[n-1],n-1),helper(wt,val,w,n-1))
        else:
            return helper(wt,val,w,n-1)
            
    return helper(wt,val,w,n)
