import sys
from math import factorial # 팩토리얼 받아오고
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수
for i in range(t) :

    n, m = map(int, input().split()) # 조합할 숫자

    print( factorial(m) // (factorial(m-n) * factorial(n)) ) # mCn 을 수학적인 식으로 풀어내면 이렇다.