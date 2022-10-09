# 1. n을 입력받기 : 1 <= n <= 1000
n = int(input())

# 2. n = 0 일때, n = 1일 때 초기화
N = [0 for _ in range(n + 1)]
N[0] = 1
N[1] = 2

# 3. DP
for i in range(2, n):
    N[i] = N[i - 1] + N[i - 2]

print(N[n - 1] % 10007)