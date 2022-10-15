import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1_max = arr1[0]
    arr2_max = arr2[0]

    for i in range(1, n):
        tmp_arr1_max = max(arr1[i] + arr2_max, arr1_max)
        arr2_max = max(arr2[i] + arr1_max, arr2_max)
        arr1_max = tmp_arr1_max

    print(max(arr1_max, arr2_max))