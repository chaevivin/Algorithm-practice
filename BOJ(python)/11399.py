import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()
temp = 0
hap = 0

for i in time:
  temp += i
  hap += temp

print(hap)
