number = 4

memo = {} # i -> fib value
def fib(n):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = 1
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
    
answer = fib(number)
print(answer)
        