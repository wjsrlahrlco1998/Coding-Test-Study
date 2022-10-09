def calcPoint(apeach_board, lion_board):
    # 1. 어피치와 라이언의 전체 점수를 각각 저장할 변수 선언
    apeach_score = 0
    lion_score = 0

    # 2. for 문을 이용하여 과녁의 점수 계산
    for i in range(11):
        # 1) 과녁에 꽂힌 화살의 개수 어피치와 라이언 모두 0개로 같은 경우 : 점수변화 없음
        if apeach_board[i] == lion_board[i] == 0:
            continue    
        # 2) 과녁에 꽂힌 화살의 개수가 어피치가 라이언과 같거나 큰 경우 : 어피치의 점수 +
        if apeach_board[i] >= lion_board[i]: 
            apeach_score += 10 - i
        # 3) 과녁에 꽂힌 화살의 개수가 라이언이 더 큰 경우 : 라이언의 점수 +
        else:
            lion_score += 10 - i
    
    # 3. 라이언 점수 - 어피치 점수 리턴
    return lion_score - apeach_score

def DFS(idx, arrow_n, apeach_board, lion_board):
    global answer, point

    # 2. 화살의 개수가 0보다 작은 경우 return
    if arrow_n < 0:
        return
    
    # 3. 최대깊이(11)까지 탐색이 이루어진 경우 과녁의 점수를 계산
    if idx > 10:
        diff = calcPoint(apeach_board, lion_board)
        # 1) 라이언 - 어피치의 차가 0보다 같거나 작은 경우 과녁을 업데이트 하지않는다([-1] 그대로)
        if diff <= 0:
            return
        # 2) 라이언 - 어피치의 차가 point보다 큰 경우 과녁을 업데이트한다.
        if diff > point:
            point = diff
            answer = [lion_board[i] for i in range(11)]
            answer[10] += arrow_n
        return
    
    # 4. 재귀 탐색
    # 1) 라이언이 어피치보다 더 많은 화살을 쏘는 경우 탐색
    lion_board[10 - idx] = apeach_board[10 - idx] + 1
    DFS(idx + 1, arrow_n - lion_board[10 - idx], apeach_board, lion_board)
    # 2) 라이언이 쏘지 않는 경우 탐색
    lion_board[10 - idx] = 0
    DFS(idx + 1, arrow_n, apeach_board, lion_board)

def solution(n, info):
    # 1. DFS에 사용할 전역변수 선언
    global answer, point
    answer = [-1]
    point = 0
    
    # 2. DFS(깊이 우선 탐색 시작)
    DFS(0, n, info, [0 for _ in range(11)])

    return answer