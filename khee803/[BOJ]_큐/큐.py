from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    text = list(sys.stdin.readline().split())
    if text[0] == 'push':
        queue.append(text[1])
    elif text[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif text[0] == 'size':
        print(len(queue))
    elif text[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif text[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif text[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])