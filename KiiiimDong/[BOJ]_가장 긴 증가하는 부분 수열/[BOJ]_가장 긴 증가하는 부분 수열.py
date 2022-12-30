n = int(input()) # 수열길이
number_list = list(map(int, input().split())) # 전체수열 리스트로 받아줌.
dp = [1] * n # dp 1로 초기화.(최소1이니깐)

for i in range(1, n): # 2 ~ n 번째까지 
    for j in range(i):  
        if number_list[i] > number_list[j]: #i는 고정시키고 j를 바꿔가면서
            dp[i] = max(dp[i], dp[j] + 1) # dp를 초기화 시킴.

print(max(dp)) # dp돌아간 것 중에서 max값 출력.