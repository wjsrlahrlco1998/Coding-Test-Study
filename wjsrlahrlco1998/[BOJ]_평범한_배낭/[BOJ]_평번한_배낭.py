# 1. 물품의 수 N과 최대 무게 K 입력 : 1 <= N <= 100, 1 <= K <= 100000
N, K = map(int, input().split())

# 2. 배낭 정의
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 3. 각 물품의 무게와 가치 입력
items = [(0, 0)]                                    # 0은 물건이 없는 상태를 의미 (무게 0, 가치 0)

for _ in range(N):
    weight, value = map(int, input().split())
    items.append((weight, value))

# 4. Dynamic programming
# 1 ~ K 무게까지 모든 최적의 무게 값을 구한다.
for i in range(1, N + 1):               # 1 ~ N번 물건까지 반복
    for j in range(1, K + 1):           # 1 ~ K무게까지 반복    
        weight = items[i][0]            # i 번째 물건의 weight
        value = items[i][1]             # i 번째 물건의 value

        if j < weight:                  # i 번째 물건의 무게가 DP 진행중인 무게보다 큰 경우 -> 물건을 추가할 수 없음
            bag[i][j] = bag[i - 1][j]   
        else:                           # 현재 배낭에 담긴 무게보다(이전 DP로 구한 값) 현재 i 번째 물건을 추가했을 때 중 더 큰 값으로 배낭 업데이트
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])

print(bag[N][K])