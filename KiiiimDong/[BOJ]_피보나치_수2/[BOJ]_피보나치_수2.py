# 1. n 입력
n = int(input())

# 2. dp table 초기화
dp = [0] * (n+1)

# 3. 초기값 설정
dp[0] = 0
dp[1] = 1

# 4. 2부터 n까지 dp진행
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# 5. dp[n] : dp테이블의 n번째 원소 출력.
print(dp[n])
