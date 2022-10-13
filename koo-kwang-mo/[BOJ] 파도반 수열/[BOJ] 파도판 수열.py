Times = int(input())#시행 횟수 입력 받기
list = []#몇 번 째 삼각형을 받을 지에 대한 숫자 저장
for i in range(Times):
    k = int(input())
    list.append(k)

def dp_t(n):#dp식을 매번 초기화하여 사용하기 위해 함수화
    #이하 5개 항은 초기값
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    #점화식
    if n>=5:
        for i in range(5,n):
            dp[i] = dp[i-1] + dp[i -5]
    return dp

for i in list:
    dp = [0] * i
    if i >= 1 and i<=3:
        print(1)
    elif i>=3 and i <= 4:
        print(2)
    else:
        print(dp_t(i)[i-1])