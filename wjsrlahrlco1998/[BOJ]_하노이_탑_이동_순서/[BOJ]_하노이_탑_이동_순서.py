# 1. 원판의 개수 N 입력 : 1 <= N <= 20
N = int(input())

# 2. 하노이 탑 재귀함수 정의
count = 0                                   # 옮긴 횟수를 저장
trace = []                                  # 옮긴 경로를 저장

'''
<원리>
1. 마지막 원판을 제외하고는 sub 장대로 모두 옮긴다.
2. 마지막 원판이 하나 남았을 경우에는 target 장대로 마지막 원판을 옮긴다.
3. 이후 sub 장대에 있는 모든 원판을 target 장대로 옮긴다.
'''
def hanoi(n, start, target, sub):
    global count

    # 1) 만약 남은 원반이 1개라면 return
    if n == 1:
        trace.append([start, target])
        count += 1
        return
    
    # 2) start에서 sub 장대로 옮김
    hanoi(n - 1, start, sub, target)
    trace.append([start, target])
    count += 1
    # 3) sub 장대에서 target 장대로 옮김
    hanoi(n - 1, sub, target, start)

# 3. 결과
hanoi(N, 1, 3, 2)
print(count)
for a, b in trace:
    print(a, b)