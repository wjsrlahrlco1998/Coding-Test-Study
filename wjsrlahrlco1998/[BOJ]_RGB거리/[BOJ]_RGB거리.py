import sys
read = sys.stdin.readline

# 1. 집의 수 입력받기 : 2 <= N <= 1000
n_house = int(input())

# 2. 각 집을 칠하는 비용 입력받기 : 0 < 비용 <= 1000인 자연수
costs = []

for _ in range(n_house):
    costs.append(list(map(int, input().split())))

# 3. DP
for i in range(1, n_house):
    # 1) 다음 집을 빨강(R)으로 색칠하는 경우
    costs[i][0] = min(costs[i - 1][1], costs[i - 1][2]) + costs[i][0]
    # 2) 다음 집을 초록(G)으로 색칠하는 경우
    costs[i][1] = min(costs[i - 1][0], costs[i - 1][2]) + costs[i][1]
    # 3) 다음 집을 파알(B)으로 색칠하는 경우
    costs[i][2] = min(costs[i - 1][1], costs[i - 1][0]) + costs[i][2]

print(min(costs[n_house - 1]))