import sys
input = lambda : sys.stdin.readline().strip()

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]

dp=[[0]*n for i in range(n)] # 방문 횟수 
dp[0][0]=1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        
        d=i+a[i][j] # 아래쪽
        r=j+a[i][j] # 오른쪽 
        
        if d < n: 
            dp[d][j] += dp[i][j]
        if r < n:
            dp[i][r] += dp[i][j]

print(dp[n-1][n-1])