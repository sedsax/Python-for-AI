def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
def factorial_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        memo[n] = n * factorial_memoization(n - 1, memo)
        return memo[n]
    
def factorial_dynamic_programming(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]

if __name__ == "__main__":
    n = 10  
    
    print(f"Loop ile {n}! = {factorial_loop(n)}")
    print(f"Recursive ile {n}! = {factorial_recursive(n)}")
    print(f"Memoization ile {n}! = {factorial_memoization(n)}")
    print(f"Dynamic Programming ile {n}! = {factorial_dynamic_programming(n)}")

