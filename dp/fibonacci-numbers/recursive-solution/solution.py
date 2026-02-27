number = 4

def fib(n):
    # base case
    if n < 2:
        return 1
    
    # recursive step
    return fib(n-1) + fib(n-2)

answer = fib(number)
print(answer)