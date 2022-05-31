import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

min_data = min(data)
max_data = max(data)

print(min_data, max_data)
