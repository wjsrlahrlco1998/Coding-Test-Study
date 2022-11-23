import sys

# 1. 문자열의 개수 N, M 입력 : 1 <= N, M <= 10,000
N, M = map(int, sys.stdin.readline().split())

# 2. N개의 문자열 입력 : 집합 S에 포함된 문자열
S = set()

for _ in range(N):
    S.add(sys.stdin.readline())

# 3. M개의 문자열 입력
non_S = list()

for _ in range(M):
    non_S.append(sys.stdin.readline())

# 4. M개의 문자열 중 집합 S에 포함되어있는 문자열의 개수
included_str_num = 0

for str in non_S:
    if str in S:
        included_str_num += 1

# 5. 결과 출력
print(included_str_num)