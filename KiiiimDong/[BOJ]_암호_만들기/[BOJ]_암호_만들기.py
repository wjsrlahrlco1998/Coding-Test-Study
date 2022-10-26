# 1. 필요한 것들 import 및 input 받아주기
from itertools import combinations # 조합 
import sys # sys
input = sys.stdin.readline # input 바꿔주기
L, C = map(int, input().split()) # L(암호길이)과 C(사용할수 있는 문자 수) 받아주기
code = input().rstrip().replace(' ', '') # 사용할 수 있는 문자 C 개 나열.
code = sorted(code) # 사용할 수 있는 문자를 정렬(a부터 z까지 가는 오름차순 으로)

combi = list(combinations(code,L)) # code에서 L개를 뽑아서 가능한 조합을 다 나타냄. 

# print(combi)
# 바로 위의 print코드는 combination 궁금하면 실행해보면 되는코드

# 2. combination에서 'aeiou' 중 하나를 포함하고 있는지, 나머지 자음 2개이상을 포함하고 있는지를 검사하고, 있을때만 프린트한다.
for i in combi: # 조합 구한거를 하나씩 받아온다.
    cnt1=0 # 모음을 세어줄 cnt
    cnt2=0 # 자음을 세어줄 cnt
    for temp in i: # 조합 구한거 하나 떼온거를 하나씩 뜯어서 검증하는 코드
        if temp in "aeiou": # 하나씩 뜯어서 모음일 때
            cnt1 +=1 # 모음 카운트 +1
        else: # 자음일 때
            cnt2 +=1 # 자음 카운트 +1

    if cnt1>=1 and cnt2>=2: # 모음이 한개 이상이고, 자음이 2개이상일때
        print(''.join(i)) # 조합 구한거를 이어붙여준다.