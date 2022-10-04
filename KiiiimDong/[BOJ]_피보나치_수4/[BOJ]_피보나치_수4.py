# 1. n 받기(n번째~)
n = int(input())

# 2. dp를 n 범위 나눠서 진행
if n == 0: # 0일때 0
    print(0)
elif n == 1: # 1일때 1
    print(1)
else:
    dp = [0] * (n+1) # 0이 들어간 배열로 초기화
    dp[0] = 0 # 0일때
    dp[1] = 1 # 1일때
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2] # 점화식 그대로 이용.
    print(dp[n]) # n번째 피보나치 수 출력.