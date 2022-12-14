n = int(input()) # 집의 개수
dp = [list(map(int,input().split())) for _ in range(n)] # dp table (3 * n)

for i in range(1,n):
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2]) # 빨강색일때 + 초록이랑 파랑중에 작은값
    dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2]) # 초록색일때 + 빨강이랑 파랑중에 작은값
    dp[i][2] = dp[i][2] + min(dp[i-1][0], dp[i-1][1]) # 파란색일때 + 빨강이랑 초록중에 작은값

print(min(dp[n-1])) # dp가 1부터 n-1까지 돌아가니깐 dp[n-1]의 min값을 계산.(처음에 초기값세팅 되있어서 1 들어오면 제일 처음 dp[0]값 중 min으로 계산)