def factorial_dynamic(n):
    if n == 0:
        return 1
    return n * factorial_dynamic(n-1)

def factorial_memo(f):
    memo = {}
    def inner(num):
        if num not in memo:
            memo[num] = f(num)
        return memo[num]
    return inner

@factorial_memo
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

number = 6
print(f'Factorial of {number} is {factorial_dynamic(number)} - Dynamic Programming \n')
print(f'Factorial of {number} is {factorial(number)} - Memoization \n')
