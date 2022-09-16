def solution(s):
    # 1. return 변수 선언
    binary_count = 0 # 이진 변환 횟수
    remove_zero_count = 0 # 제거된 모든 0의 개수

    # 2. 이진 변환 반복
    while s != "1":
        # 1) 문자열에서 0의 개수 세기
        s_zero_count = s.count("0")
        remove_zero_count += s_zero_count

        # 2) 문자열 s의 길이
        s_len = len(s)

        # 3) 0을 제거한 문자열 선언
        s_removed = "1" * (s_len - s_zero_count)

        # 4) 문자열의 길이 이진 변환
        s_binary = bin(len(s_removed))[2:]
        binary_count += 1

        # 5) 문자열 s 갱신
        s = str(s_binary)

    # 3. 결괏값 저장
    answer = [binary_count, remove_zero_count]

    return answer
