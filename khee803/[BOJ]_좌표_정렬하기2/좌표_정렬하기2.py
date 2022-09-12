import sys

N = int(sys.stdin.readline())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots.sort()
dots.sort(key=lambda x:x[1])

for i in range(N):
    print(*dots[i])