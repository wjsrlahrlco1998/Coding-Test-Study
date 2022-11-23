import sys

# 1. 1 ~ 10000까지 모든 정수 정의
integer_num = set([i for i in range(1, 10001)])

# 2. Self Num이 아닌 수를 담을 Set 정의
non_self_num = set()

# 3. Generator 정의 : 숫자 생성자
def generator():

    # 1) 1 ~ 10000까지 모든 정수의 Non self num을 구한다.
    for i in range(1, 10001):
        for j in str(i):
            i = i + int(j)
        non_self_num.add(i)

    # 2) 모든 정수 - Non self num = self num
    self_num = sorted(integer_num - non_self_num)

    # 3) self num 출력
    for i in self_num:
        print(i)

# 4. 결과
generator()