n = int(input())
s = list(map(int, input().split()))
dp = []#해당 인덱스의 상자가 쌓인 갯수 저장.
dp.append(1)#초기값 1
for i in range(1, n):
    d = []#상자가 쌓인 갯수 임시 저장
    for j in range(i):
        if s[i] > s[j]:#
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))