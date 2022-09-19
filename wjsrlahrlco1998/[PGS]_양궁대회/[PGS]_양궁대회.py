def solution(n, info):
    answer = []

    # 1. 현재 어피치가 획득한 점수
    apitch_score = 0
    for i in range(len(info)):
        if info[i] > 0:
            apitch_score += 10-i

    # 2. 어피치의 과녁을 참고하여 각 과녁의 점수당 화살의 효율 점수를 구한다.
    eff_arrow_info = [0] * 11
    for i in range(len(info)):
        eff_arrow_score = (10 - i) / (info[i] + 1) # 과녁 점수 / 맞춰야할 화살의 수 = 화살 한 개당의 효율 점수
        if info[i] > 0: # 만약 화살이 있으면 그 효율은 2배(점수를 뺏기 때문)
            eff_arrow_score = eff_arrow_score * 2
        eff_arrow_info[i] = (eff_arrow_score, info[i] + 1, i) # (효율점수, 쏘아야할 화살의 수, 과녁 인덱스)

    # 3. 효율 점수 리스트를 정렬
    eff_arrow_info = sorted(eff_arrow_info, key = lambda x : (x[0], x[2]), reverse=True)
    print(eff_arrow_info)

    # 4. 효율 점수 리스트를 바탕으로 과녁 쏘기
    lion_score = 0
    lion_info = [0] * 11
    limited_n_arrow = n

    for i in eff_arrow_info:
        if (i[1] > 1) & (limited_n_arrow - i[1] >= 0):
            lion_info[i[2]] = i[1]
            lion_score += 10 - i[2]
            apitch_score -= 10 - i[2]
            limited_n_arrow -= i[1]
        elif (limited_n_arrow - i[1] >= 0):
            lion_info[i[2]] = i[1]
            lion_score += 10 - i[2]
            limited_n_arrow -= i[1]

        if limited_n_arrow == 0:
            break
    
    if limited_n_arrow > 0:
        lion_info[-1] += limited_n_arrow
        limited_n_arrow = 0

    if lion_score <= apitch_score:
        answer = [-1]
    else:
        answer = lion_info

    return answer

print("result")
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
print(solution(3, [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]))
print(solution(2, [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
"""
<메모>
1. 어피치의 점수 0개를 뺏는 경우 ~ n개를 뺏는 경우
2. '1'의 과정을 시행해서 라이언의 합계 점수가 어피치의 합계 점수를 넘으면 return

<조건>
1. 라이언은 가장 큰 점수차로 이기는 경우가 Best
2. 가장 큰 점수차로 이기는 경우가 여러 개일 경우, 낮은 점수를 많이 쏜 경우가 Best
"""