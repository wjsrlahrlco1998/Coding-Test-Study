import sys

read = sys.stdin.readline

# 1. 회의 수 입력 : 1 <= N <= 100000
n_meetings = int(input())

# 2. 회의들의 정보 입력 : 0 <= time <= 2 ** 31 - 1
meetings_info = []

for _ in range(n_meetings):
    start, end = map(int, input().split())
    meetings_info.append((start, end))

# 3. 최대 회의의 개수 찾기 

# 1) 끝나는 시간이 빠른 회의 중 시작하는 시간이 빠른 순으로 정렬
meetings_info.sort(key = lambda x : (x[1], x[0]))

# 2) 회의 선택
greedy_meetings = 0                 # 회의 수 카운트
last_time = 0     # 처음 선택된 회의의 끝나는 시간

for start_time, end_time in meetings_info:   
    if start_time >= last_time:          # 회의 시작시간이 앞의 회의의 끝나는 시간보다 같거나 큰 경우만 회의 가능
        greedy_meetings += 1
        last_time = end_time

# 4. 결과 출력
print(greedy_meetings)