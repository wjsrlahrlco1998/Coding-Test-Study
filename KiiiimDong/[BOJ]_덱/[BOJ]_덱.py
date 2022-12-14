import sys 
input = sys.stdin.readline
deque = []
n  = int(input())
for i in range(n):
    command = input().rstrip() # readline으로 받아서 rstrip
    if "push" in command : # push front 이거나 push back 일때
        a,b = command.split() # 문자랑 숫자 나누기
        if a == 'push_front': 
            deque.insert(0,b) # front일때, 덱의 제일 앞에 넣는다.(0번째에 b를 넣는다.)
        elif a == 'push_back': 
            deque.append(b) # back 일때, 덱의 제일 뒤에 넣는다.
    elif "pop_front" == command : # pop front일때
        if len(deque) == 0: # 덱이 비어있으면
            print(-1) # -1 출력
        else: 
            print(deque.pop(0)) # 덱에 들어있을 때는 앞에서부터 꺼내서 출력
    elif "pop_back" == command: # pop back일때
        if len(deque) == 0: # 덱이 비어있으면
            print(-1) # -1 출력
        else: 
            print(deque.pop(-1)) # 덱이 비어있지 않을 때 뒤에서부터 꺼내서 출력
    
    elif 'size' == command: # size일때
        print(len(deque)) # len을 출력
    elif 'empty' == command: # empty일때
        if len(deque) == 0: # 덱이 비어있으면
            print(1) # 1 출력
        else: # 덱이 비어있지 않으면
            print(0) # 0 출력
    elif 'front' == command: # front일때
        if len(deque) == 0: # 덱이 비어있으면
            print(-1) # -1 출력
        else: 
            print(deque[0]) # 덱이 비어있지 않을 때 제일 앞에 있는거 출력
    elif 'back' == command: # back일때
        if len(deque) == 0: # 덱이 비어있으면
            print(-1) # -1 출력
        else: 
            print(deque[-1]) # 덱이 비어있지 않을 때 제일 뒤에 있는거 출력