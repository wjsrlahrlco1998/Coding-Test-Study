from collections import deque
import sys

# 1. 명령의 수 입력 : 1 <= N <= 10000
N = int(sys.stdin.readline())

# 2. 명령 입력
stack = deque()

for _ in range(N):
    commands = sys.stdin.readline().split()
    command = commands[0]

    if len(commands) > 1:
        param = int(commands[1])
    
    if command == "push":
        stack.append(param)
        continue

    if command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
        continue

    if command == "size":
        print(len(stack))
        continue

    if command == "empty":
        if stack:
            print(0)
        else:
            print(1)
        continue

    if command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
        continue