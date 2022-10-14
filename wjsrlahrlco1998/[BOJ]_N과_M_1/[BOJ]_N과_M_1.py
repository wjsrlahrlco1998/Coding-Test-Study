import sys

read = sys.stdin.readline

# 1. N과 M 입력받기 : 1 <= M <= N <= 8 인 자연수
N, M = map(int, input().split())

# 2. 1부터 N까지 길이가 M인 중복없는 수열을 모두 구하기
decision_space = []

def backtracking():
    if len(decision_space) == M:                    # 길이가 M이면 출력!
        print(" ".join(map(str, decision_space)))
        return
    
    for i in range(1, N + 1):                       # 1부터 N + 1까지 진행하면서 중복이 아니면 append
        if i not in decision_space:
            decision_space.append(i)
            backtracking()
            decision_space.pop()                    # 원하는 결과를 출력하게되면 pop을 통하여 decision space를 하나씩 이동한다.

# 3. backtracking 실행
backtracking()