n = int(input())
s = list(map(int, input().split()))
dp = []#해당 인덱스의 상자가 쌓인 갯수 저장.
dp.append(1)#초기값 1
for i in range(1, n):
    d = []#상자가 쌓인 갯수 임시 저장
    for j in range(i):
        if s[i] > s[j]:# i번째가 충분히 클 때 앞의 경우의 수에 대해 + 1해줌, 매 회차에 대해 상자 넣은 갯수 갱신
            d.append(dp[j] + 1)
    if not d:#D가 비어 있을 때, 2번쨰 인덱스가 첫 번째보다 작은 경우
        dp.append(1)
    else:#최대값 저장.
        dp.append(max(d))
print(max(dp))