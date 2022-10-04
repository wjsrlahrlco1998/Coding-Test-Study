# 1. 재귀함수 활용.
def fib(n):
    global cnt1 # 밑에서 써야해서 global로 선언
    
    cnt1 += 1
    if (n == 1 or n == 2): # n이 1이나 2일때는 실행횟수가 늘어나지 않는다.
        cnt1 -= 1 # cnt += 1 해준걸 cnt -= 1로 다시 원래대로 돌려 놓는다.
        return 1 # 문제에서 제시한대로 그냥 옮겨 적은 것 뿐
    else: 
        return (fib(n - 1) + fib(n - 2)) # 문제에서 제시한대로 그냥 옮겨 적은 것 뿐

# 2. dp(동적프로그래밍)활용
def fibonacci(n):
    global cnt2 # 밑에서 써야해서 global로 선언

    # 피보나치 dp 식대로 그대로 적음
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt2 += 1
    return dp[n]
# 3. 출력부분
n = int(input()) # n 받아서
cnt1 = 0 # cnt 초기화
cnt2 = 0 # cnt 초기화
fib(n) # 재귀함수로 작동
fibonacci(n) # dp로 작동
print(cnt1+1, cnt2) # 재귀함수 실행횟수, dp 실행횟수 출력. 재귀함수는 자기자신을 부르는 거라서 +1