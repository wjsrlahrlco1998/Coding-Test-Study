# 1. N과 M 입력
N, M = map(int, input().split())

# 2. Decision space 정의
decision_space = []

# 3. BackTracking
def backtracking():
    if len(decision_space) == M:
        print(" ".join(map(str, decision_space)))
        return

    for i in range(1, N + 1):
        if len(decision_space) > 0:             # decision space에 하나라도 원소가 들어가 있는 경우
            if decision_space[-1] <= i:         # decision space의 마지막 원소가 i보다 작거나 같은 경우 (비 내림차순 정렬을 위함)
                decision_space.append(i)
                backtracking()
                decision_space.pop()
        else:                                   # decision space에 원소가 하나도 없는 경우 : 그냥 하나 추가
            decision_space.append(i)
            backtracking()
            decision_space.pop()

# 4. 결과 출력
backtracking()
