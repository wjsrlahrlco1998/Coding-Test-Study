import sys
input = sys.stdin.readline
S = int(input()) # 수들의 최종합
n = 0 # S와 크기 비교를 하며 S 보다 커질 때까지 숫자를 늘려갈 변수
cnt = 0 # 정답(자연수의 개수 세어줄 변수)
m = 0 # 1부터 1씩 늘려가면서 n에 더해줄 변수
while True:
    if S < n: # S를 초과해버릴 때 끝낸다.
        break
    else:
        m += 1  # m을 하나늘려주면서
        n = n + m  # 기존의 n이랑 더해준게 새로운 n이다.      
        cnt += 1 # 한번 더할때마다 카운트
print(cnt-1) # 맨 마지막 초과하는 것 까지 계산되므로 하나를 빼준값을 프린트.
