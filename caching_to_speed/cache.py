from functools import cache
import time


# We can keep this recursive and still make it fast 
# w/o chainging to iterative function by caching the result    

@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# there is a recursion limit in python.. 400 perhaps?
start = time.time()
print(fibonacci(300))
end = time.time()

print(end-start)

