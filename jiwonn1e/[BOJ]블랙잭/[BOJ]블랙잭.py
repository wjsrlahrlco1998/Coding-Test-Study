n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for first in range(n-2):
    for second in range(first +1,n-1):
        for third in range(second +1, n):
            sum=card[first]+card[second]+card[third]
            if sum <= m:
                result=max(result, sum)
print(result)