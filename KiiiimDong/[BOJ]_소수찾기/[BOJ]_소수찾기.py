n = int(input())
case = list(map(int, input().split()))
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

cnt = 0

for i in range(n):
    if case[i] == 1:
        continue
    elif is_prime_number(case[i]) == True:
        cnt += 1
    else:
        continue
print(cnt)