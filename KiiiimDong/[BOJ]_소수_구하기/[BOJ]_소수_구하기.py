# 1. 기본세팅
import math # 수학관련(sqrt쓰기위함)
import sys # sys.stdin.readline불러오기위함
input = sys.stdin.readline # 인풋 대체

# 2. 인풋 받아주고 기본 설정
m, n  = map(int, input().split()) # m이상 n 이하의 소수를 구해야한다.
array = [True for i in range(n+1)] # 모든수가 소수인 것으로 초기화.

# 3. 에라토스테네스의 체 적용
for i in range(2, int(math.sqrt(n)+1)): # 2~ n까지
    if array[i] == True: 
        # 배수 (처음에 2로 시작)
        j = 2
        while i * j <= n: # j를 계속 증가시키면서 n이 넘으면 멈춘다.
            array[i * j] = False # 배수가 되는 애들 제거(False준다.)
            j += 1 # 배수를 증가시키면서 배수를 제거시키는 것

# 4. 조건에 해당하는 모든 소수 출력
for i in range(2, n+1):
    if array[i] and i >=m and i <= n: # array[i]가 True일때, 그리고 m과 n사이의 i를 가질때
        print(i) # i를 출력한다.
