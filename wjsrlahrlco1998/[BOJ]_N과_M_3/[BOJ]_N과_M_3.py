# 1. N과 M 입력 받기 : 1 <= N, M <= 7
N, M = map(int, input().split())

# 2. Decision space
decision_space = []

# 3. 수열 찾기 : Backtracking 정의
def backtracking():
    # 1) 길이가 M이면 출력 후 return
    if len(decision_space) == M:
        print(" ".join(map(str, decision_space)))
        return
    
    # 2) 1부터 N까지 dfs
    for i in range(1, N + 1):
        decision_space.append(i)
        backtracking()
        decision_space.pop()

# 4. 결과 출력
backtracking()