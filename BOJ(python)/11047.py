import sys

n, k = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline().strip()) for i in range(n)]

count = 0

for i in reversed(money):
  if k >= i:
    count += k // i
    k %= i
    
print(count)
