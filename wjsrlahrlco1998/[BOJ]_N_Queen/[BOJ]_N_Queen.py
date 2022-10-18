import sys
read = sys.stdin.readline()

# 1. N 입력 : 1 <= N < 15
N = int(read)

# 2. Decision space 정의
decision_space = [-1 for _ in range(N)]

# 3. Backtracking
n_method = 0                # 퀸을 놓는 방법의 수

def isPromise(x):
    for i in range(x):
        # 1) 퀸을 놓았을 때, 해당 열에 퀸이 존재하거나, 대각선 상에 퀸이 존재하는 경우는 False를 리턴
        if (decision_space[x] == decision_space[i]) or (abs(decision_space[x] - decision_space[i]) == abs(x - i)):
            return False
    
    # 2) 퀸을 놓았을 때, 공격동선과 겹치지 않는다면 True를 리턴
    return True

def backtracking(x):
    global n_method

    # * 탈출조건 : x가 최대 깊이 즉, 최대 행 + 1까지 도달한 경우 퀸을 겹치지 않게 놓은 것이므로 방법 + 1
    if x == N:
        n_method += 1
        return

    # 1) 퀸을 놓는다.
    for i in range(N):
        decision_space[x] = i               # (x, i)에 퀸을 놓음
        if isPromise(x):                    # (x, i)에 퀸을 놓은 것이 적절한지 판단.
            # 2) 퀸을 놓았을 때, 유망한 경우 다음 행으로 이동
            backtracking(x + 1)

# 4. Backtracking 0행부터 시작
backtracking(0) 

# 5. 결과
print(n_method)