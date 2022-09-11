def solution(s):
    # 1. 공백을 기준으로 split한 후, map을 이용하여 자료형을 int형으로 바꾸고 다시 list형태로 변환한다.
    nums = list(map(int, s.split(" ")))

    # 2. 최소값과 최대값의 초기화
    min = 9999
    max = -9999

    # 3. 최솟값은 min에 최댓값은 max에 저장
    for i in nums:
        if i < min:
            min = i
        
        if i > max:
            max = i

    # 4. max와 min의 자료형을 str로 변환
    min = str(min)
    max = str(max)

    # 5. join을 이용하여 "최솟값 최댓값"의 형태로 만들기.
    answer = " ".join([min, max])

    return answer