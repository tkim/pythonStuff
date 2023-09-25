# Naive approach
""" def fib(n):
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n -2)
    return result
print (fib(7)) """

# Elegant approach = memoization
# DP = Recrusion + Memoization
memo = {}

def fib(n):

    if n in memo:
        return memo[n]

    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    
    memo[n] = result
    return result

print(fib(50))

