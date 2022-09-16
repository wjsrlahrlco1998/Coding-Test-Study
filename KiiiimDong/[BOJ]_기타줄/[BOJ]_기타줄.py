import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
package_price = 10000
single_price = 10000 
for i in range(m):
    a, b = map(int, input().split())
    
    if a < package_price:
        package_price = a
    if b < single_price:
        single_price = b
pp = package_price
sp = single_price


package, single = 0,0
if sp * 6 >= pp: 
    package = n // 6
    single = n % 6
    
    if pp <= (single * sp):
        package +=1
        single = 0
else:
    single = n

print(package * pp + single * sp)