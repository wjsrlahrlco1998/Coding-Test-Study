from statistics import mean, median
from collections import Counter
import sys

# 1. 입력할 개수 N : N (1 <= N <= 500000)
N = int(sys.stdin.readline())

# 2. 정수 입력 : 정수의 절대값은 4000을 넘지 않는다.
integers = []                                           # 정수를 입력받을 리스트 선언

for _ in range(N):
    integer = int(sys.stdin.readline())
    integers.append(integer)

# 3. 산술평균 구하기
mean_integer = int(round(mean(integers), 0))

# 4. 중앙값 구하기
median_integer = median(integers)

# 5. 최빈값 구하기
most_integer = Counter(integers).most_common()
most_values = []

if len(most_integer) > 1:
    if most_integer[0][1] == most_integer[1][1]:
        for i in range(0, len(most_integer)):
            if most_integer[i][1] == most_integer[0][1]:
                most_values.append(most_integer[i][0])
            else:
                break
    else:
        most_values.append(most_integer[0][0])
else:
    most_values.append(most_integer[0][0])

if len(most_values) > 1:
    most_values.sort()
    most_value = most_values[1]
else:
    most_value = most_values[0]

# 6. 범위 계산 : 최댓값 - 최솟값
range_integer = abs(max(integers) - min(integers))

print(mean_integer)
print(median_integer)
print(most_value)
print(range_integer)
