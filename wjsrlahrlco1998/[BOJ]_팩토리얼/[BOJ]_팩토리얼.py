import sys
sys.setrecursionlimit(50000)             # 재귀 용량 늘리기

# 1. 정수 N 입력 : 1 <= N <= 12
N = int(input())

# 2. 팩토리얼 재귀함수 정의
def factorial(x):
    if x == 0:
        return 1
    
    return x * factorial(x - 1)

# 3. 결과 출력
print(factorial(N))