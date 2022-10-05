# 1. 시간초과 나지 않기 위해서 input을 바꿔줌
import sys
input = sys.stdin.readline

# 2. n과 m, 그리고 그 갯수만큼 숫자가 나열된 리스트 들을 받아줌
n = int(input()) # n개
n_list = set(map(int, input().split())) # set으로 받아줌
m = int(input()) # m개
m_list = list(map(int, input().split())) # list로 받아줌

# 3. m_list에서 원소를 하나씩 꺼내서 n_list에 존재하면 1 아니면 0으로 바꿔준다.
for i in range(len(m_list)):
    if m_list[i] in n_list: # n_list에 존재하면 
        m_list[i] = 1 # 1 
    else: # n_list에 존재하지 않을 때
        m_list[i] = 0 # 0

# 4. 1과 0으로 바뀐 m_list를 출력한다
for result in m_list: # m_list에서 하나씩 꺼내서
    print(result) # 출력