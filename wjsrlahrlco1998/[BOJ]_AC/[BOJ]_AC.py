from collections import deque
import sys

# 1. 테스트 케이스 T 입력 : 1 <= T <= 100
T = int(sys.stdin.readline())

# 2. 각 테스트 케이스 별 입력
for _ in range(T):
    # 1) 수행할 함수 p 입력 : p의 길이는 1 <= p <= 100000
    p = sys.stdin.readline().rstrip()

    # 2) 정수 배열의 길이 n
    n = int(sys.stdin.readline())

    # 3) 배열 입력
    array = deque(eval(sys.stdin.readline()))                      # 문자열 형태의 list를 list로 deque로 변환

    error = False                                                  # error 여부를 판단할 함수

    # 4) "R" 명령이 쌓인 개수를 저장할 변수 선언
    r_stack = 0

    # 5) 명령어 실행
    for func in p:

        if func == "R":
            r_stack += 1
            continue
        
        if func == "D":
            if array:                                               # array가 비어있지 않으면 popleft 실행
                if r_stack % 2 == 0:                                # r_stack이 짝수이면 popleft
                    array.popleft()
                else:                                               # r_stack이 홀수이면 pop                    
                    array.pop()                                         
            else:                                                   # array가 비어있으면 error = True 후 break
                error = True
                break

    if error:
        print("error")
    else:
        if r_stack % 2 == 0:
            print("["+",".join(map(str,array))+"]")
        else:
            array.reverse()
            print("["+",".join(map(str,array))+"]")