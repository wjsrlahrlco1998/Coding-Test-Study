from collections import deque # 큐를 구현하기위해서 deque을 불러옴.

N, K = map(int, input().split()) # n과 k를 입력받는다.

q = deque() # 큐 구현
result = [] # 결과를 받아줄 리스트.

for i in range(N): 
    q.append(i+1) # 1 부터 n까지 큐에 append

while q: # 큐가 빌 때까지
    for i in range(K): 
        if not i == K-1: # k번째가 되지 않을 때(i가 0부터 시작하니깐 k-1로)
            temp = q.popleft() # 큐에서 꺼내서
            q.append(temp) # 다시 큐에 넣는다. 선입선출이라 젤 뒤에로 간다.
        else: # k번째가 될 때
            temp = q.popleft() # 큐에서 꺼내서
            result.append(temp) # 결과에 넣는다.

print("<", end="") # < 를 출력하고 이어준다.
for i in range(len(result)):
    if not i == len(result)-1: # 마지막이 아닐때
        print(result[i], end=", ") # 프린트하고 ,으로 이어준다.
    else: # 마지막일 때 
        print(result[i], end=">") # 프린트하고 >으로 마무리