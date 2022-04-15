import sys

n, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in A:
	if i < x:
		print(i, end = ' ')
