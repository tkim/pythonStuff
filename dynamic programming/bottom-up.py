# Another way to look at DP. Compute the sub problem first
# This approach doesn't have function calls which is more efficient in practice.
# In this approach for fibonacci, we only need to recall the last 2 numbers in the values.

def fib(n):
    memo = {}

    for i in range(l, n + 1):
        if i <= 2:
            result = 1
        else: 
            result = memo[i - 1] + memo[i - 2]
        memo[i] = result
    
    return memo[n]
