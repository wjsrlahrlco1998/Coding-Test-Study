import sys

# 1. n 입력 : 5 <= n <= 40
n = int(sys.stdin.readline())

# 2. 호출횟수
cnt_1 = 0                               # 코드 1에 대한 호출횟수
cnt_2 = 0                               # 코드 2에 대한 호출횟수

# 2. 피보나치(재귀)
def fib(n):
    global cnt_1
    if n == 1 or n == 2:
        cnt_1 += 1
        return 1                        # 코드 1
    else:
        return fib(n-1) + fib(n-2)

# 3. 피보나치(DP)
def fibonacci(n):
    global cnt_2
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # 코드 2
        cnt_2 += 1
    
    return dp[n]

# 4. 결과
fib(n)
fibonacci(n)
print(cnt_1, cnt_2)