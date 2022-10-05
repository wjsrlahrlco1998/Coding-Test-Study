import sys

read = sys.stdin.readline

# 1. 계단의 개수 입력받기
n = int(input())

# 2. 각 계단의 점수 입력받기
stairs = []
for i in range(n):
    stairs.append(int(input()))

# 3. DP
'''
1) 도달할 계단을 i라고 가정하면
2) i - 2번째 계단을 밟았을 경우 i - 1번째 계단은 밟으면 안된다.
3) i - 3번째 계단을 밟았을 경우 i - 1번째를 필수적으로 밟는다.
'''
scores = [0 for _ in range(n + 2)]
scores[0] = stairs[0]
scores[1] = stairs[0] + stairs[1]
scores[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    scores[i] = max(scores[i - 2] + stairs[i], scores[i - 3] + stairs[i] + stairs[i - 1])

print(scores[n - 1])