#https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=python3
"""
def solution(triangle):
    n = len(triangle)
    target=0
    answer = triangle[0][0]
    for i in range(n-1):
        number = int(triangle[i+1][target])
        answer +=number
        if i+1 == n-1:
            break
        else:
            if int(triangle[i+2][target]) > int(triangle[i+2][target+1]):
                    target +=0
            elif int(triangle[i+2][target]) < int(triangle[i+2][target+1]):
                    target +=1
            elif i+2 == n-1:
                target +=0
                continue#마지막줄로 간다. 이 떄 타겟값은 상관 없음. 다음줄은 둘 다 같은 값임.
            else:
                if int(triangle[i+3][target]) > int(triangle[i+3][target+2]):
                        target +=0
                elif int(triangle[i+3][target]) < int(triangle[i+3][target+2]):
                        target +=0
                else:
                    target +=0
    return answer
"""
"""
for i in range(2**N):
    number_bin = bin(i)
    number_bin1 = str(number_bin[2:])
    #print(number_bin1.zfill(N))
    number_bin2 = number_bin1.zfill(N)
    print(number_bin2)
    list1.append(number_bin2)
"""
"""
def bin_maker(N):
    list1 = []
    for i in range(2 ** N):
        number_bin = bin(i)
        number_bin1 = str(number_bin[2:])#zfill사용을 위해 문자열화
        number_bin2 = number_bin1.zfill(N)
        list1.append(number_bin2)
    return list1
"""
"""
def bin_maker(n, N):
    number_bin = bin(n)
    number_bin1 = str(number_bin[2:])#zfill사용을 위해 문자열화 bi0101
    number_bin2 = number_bin1.zfill(N)

    return number_bin2

def solution(triangle):
    n = len(triangle)
    total_len =2**(n-1)
    list_value = []
    times = 0
    for i in range(total_len):
        value = 0
        target = 0
        num_bin = bin_maker(times, n)
        print(num_bin)
        for j in range(n):
            value += triangle[j][target]
            if int(num_bin[j]) == 0:
                target +=0
            else:
                target +=1
        list_value.append(value)
        times +=1
    answer = max(list_value)

    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]



"""
def solution(triangle):

    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for y in range(n-1):
        for x in range(len(triangle[y])):
            dp[y+1][x] = max(dp[y+1][x],dp[y][x] + triangle[y+1][x])
            dp[y+1][x+1] = max(dp[y+1][x+1],dp[y][x] + triangle[y+1][x+1])
#점화식
    print(dp)
    return max(dp[-1])
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))