import sys

read = sys.stdin.readline

# 1. 설탕의 개수 입력 받기
N = int(input())

# 2. DP를 위한 배열 공간 선언 및 초기값 설정
'''
* Default 값을 5001로 설정한 이유는 N의 범위가 3 <= N <= 5000 이기 때문
* range를 N + 3까지로 설정한 이유는 N의 최솟값이 3인데, 우리는 bag[5]의 값을 미리 초기화했다. 따라서 N + 1까지하면 out of index Error가 발생한다.
'''
bag = [5001 for _ in range(N+3)]
bag[3] = 1
bag[5] = 1

# 3. Dynamic Programming
'''
1. i는 6부터 N까지 반복한다.
2. Default 값이 5001이기 때문에, 3이나 5로 나누어 떨어지지 않는 경우는 5001 이상의 값을 갖게 된다.
'''
for i in range(6, N + 1):
    bag[i] = min(bag[i - 3], bag[i - 5]) + 1

# 4. 결과 출력
'''
* 만약 bag[i]가 5001보다 작으면 봉지에 나누어 담을 수 있는 최소의 값이 담겨있기에 그 값을 출력한다.
* bag[i]가 5001이상이면 그 N값은 봉지에 정확하게 나누어 담을 수 없기 때문에 -1을 리턴한다.
'''
if bag[N] < 5001:
    print(bag[N])
else:
    print(-1)