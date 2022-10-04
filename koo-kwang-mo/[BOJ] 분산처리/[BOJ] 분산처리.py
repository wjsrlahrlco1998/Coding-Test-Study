t = int(input())
a = []
b = []

# for문으로 t만큼 돌면서 a와 b를 입력받아 리스트에 저장한다.
for _ in range(t):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)

for i in range(t):
    # a의 1의 자리수를 com 변수에 대입
    com = a[i] % 10

    # a가 10의 배수면, 바로 10번 컴퓨터에 매칭
    if com == 0:
        print(10)
    # a의 1의 자리수가 1, 5, 6이면, 그대로 출력하면 됨
    elif com in [1, 5, 6]:
        print(com)
    # a의 1의 자리수가 4, 9이면, b제곱한 수의 1의 자리수가 2가지 경우가 있음
    elif com in [4, 9]:
        if b[i] % 2 == 0:
            print(com ** 2 % 10)
        else:
            print(com)
    # a의 1의 자리수가 2, 3, 7, 8이면, b제곱한 수의 1의 자리수가 4가지 경우가 있음
    else:
        if b[i] % 4 == 0:
            print(com ** 4 % 10)
        else:
            print(com ** (b[i] % 4) % 10)