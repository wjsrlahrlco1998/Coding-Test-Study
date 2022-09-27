import sys

read = sys.stdin.readline

# 1. 테스트 케이스 T 입력받기
T = int(input())

# 2. 테스트 케이스 횟수만큼 반복
for _ in range(T):
    # 1) 정수 n 입력 받기 : 0 < n <= 11
    n = int(input())

    # 2) 배열 선언 및 초기값 할당
    count_of_sum = [0] * 12
    count_of_sum[1] = 1
    count_of_sum[2] = 2
    count_of_sum[3] = 4

    # 3) 점화식 적용
    for i in range(4, n + 1):
        count_of_sum[i] = count_of_sum[i - 1] + count_of_sum[i - 2] + count_of_sum[i - 3]
    
    print(count_of_sum[n])