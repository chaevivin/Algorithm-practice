import sys

n = int(sys.stdin.readline())

for i in range(n):
	for j in range(n - i, 1, -1):
		print(' ', end = '')
	for k in range(0, i + 1):
		print('*', end = '')
	print()
