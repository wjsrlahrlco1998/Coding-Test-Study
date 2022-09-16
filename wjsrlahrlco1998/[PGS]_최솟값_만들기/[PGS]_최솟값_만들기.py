def solution(A,B):

    # 1. 누적합을 저장할 변수 선언
    cumulative_sum = 0

    # 2. A는 오름차순, B는 내림차순으로 정렬
    A = sorted(A, reverse=False)
    B = sorted(B, reverse=True)

    # 3. Index 0번부터 차례대로 곱함.
    for i in range(len(A)):
        cumulative_sum += A[i] * B[i]

    # 4. 누적합을 리턴
    answer = cumulative_sum

    return answer