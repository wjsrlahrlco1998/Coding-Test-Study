# 1. n팩토리얼을 만들기위한 팩토리얼과 input을 바꾸기위한 sys를 import 
import sys 
from math import factorial # 팩토리얼 불러오기
input = sys.stdin.readline # input을 리드라인으로 바꿔줌.

# 2. n 팩토리얼을 하기위한 n을 받아줌
n = int(input())

# 3. n팩토리얼의 뒤에서부터 0이 나올 때는 카운트, 아닐 때는 break
cnt = 0 # cnt 초기화
for i in str(factorial(n))[::-1]: # 팩토리얼을 뒤집은 거에서
    if i == '0': # 0이면 
        cnt += 1 # 카운트 늘려줌
    else: # 아니면
        break # break 걸어줌
print(cnt) # 카운트 된 횟수를 출력