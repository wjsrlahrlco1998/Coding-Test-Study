import sys
input = sys.stdin.readline

n = int(input()) # 상근이가 갖고있는 숫자개수
n_list = list(map(int,input().split())) # 갖고있는 숫자들.

answer = {} # 상근이가 갖고있는 숫자를 세어줄 딕셔너리

for i in n_list: # 숫자들을 하나씩 꺼내서
    if i in answer: # 딕셔너리에 이미 존재하면
        answer[i] += 1 # 딕셔너리값을 하나 추가.
    else:  # 딕셔너리에 존재하지않으면
        answer[i] = 1 # 1개로 세어줌.

m = int(input()) # 몇 개 가지고 있는 숫자 카드인지 구해야 할 숫자의 개수(검증해야할 숫자의 개수)
m_list = list(map(int,input().split())) # 검증해야하는 숫자.

for i in m_list: # 검증해야하는 숫자들을 하나씩 꺼낸다.
    if i in answer: # 딕셔너리에 저장된 값이면(한번이라도 센적 있는 숫자)
        print(answer[i], end=" ") # 해당 키에 맞는 값을 출력
    else: # 딕셔너리에 저장되어있지않으면(한번도 센적 없는 숫자.)
        print(0,end=" ") # 0을 출력.
