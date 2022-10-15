import sys

read = sys.stdin.readline

# 1. N과 M 입력
N, M = map(int, input().split())

# 2. 중복없는 오름차순 수열 구하기
decision_space = []

def backtracking():
    if len(decision_space) == M:
        print(" ".join(map(str, decision_space)))
        return

    for i in range(1, N + 1):
        if i not in decision_space:                 # 중복 check
            if len(decision_space) > 0:             # 이미 원소가 하나이상 있는 경우,
                if decision_space[-1] < i:          # 제일 마지막 원소보다 i가 커야 append : 오름차순 수열을 구해야하기 때문
                    decision_space.append(i)
                    backtracking()
                    decision_space.pop()
            else:
                decision_space.append(i)
                backtracking()
                decision_space.pop()

backtracking()