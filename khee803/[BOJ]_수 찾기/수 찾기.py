import sys

N = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))

list1.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for num in list2:
    result = binary_search(list1, num, 0, N-1)
    if result == 0:
        print("0")
    else:
        print("1")