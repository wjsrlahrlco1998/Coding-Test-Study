# 1. input 정리
import sys # input-> readline으로 치환하기 위한것
input = sys.stdin.readline
n = int(input()) # 명령개수

# 2. 큐 구현 
queue = [] # 큐를 리스트로 구현(리스트로 받아줬음)
for i in range(n):
    code = input() # 들어오는 코드
    if code[:4] == 'push': # 푸시일때
        queue.append(int(code[5:])) # 푸시뒤에 숫자를 큐에 append
    elif (code[:3] == "pop"): # 팝일때
        if (len(queue) == 0): # 들어있는게 없으면
            print(-1) # -1 출력
        else: # 들어있는게 있을 때
            a = queue[0] # 팝할거를 받아주고
            queue.pop(0) # 팝하고
            print(a) # 팝한 것을 출력한다
    elif (code[:4] == "size"): # 사이즈 일때
        print(len(queue)) # 큐의 길이로 사이즈를 출력
    elif (code[:5] == "empty"): # empty일 때
        if (len(queue) == 0): # 비어있으면 1, 아닐 때(비어있지 않을 때) 0
            print(1)
        else:
            print(0)
    elif (code[:5] == "front"): # front일 때
        if (len(queue) == 0): # 비어있으면 -1
            print(-1)
        else: # 비어있지 않을 때
            print(queue[0]) # 제일 앞에 꺼 출력
    elif (code[:4] == "back"): # back일 때
        if (len(queue) == 0): # 비어있으면 -1
            print(-1)
        else:  # 비어있지 않을 때
            print(queue[-1]) # 큐의 젤 마지막 꺼 출력.