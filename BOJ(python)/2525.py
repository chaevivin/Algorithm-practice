import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

if B + C >= 60:
	A += ((B + C) // 60)
	B = (B + C) % 60
else: 
	B += C

if A > 23:
	A %= 24

print("%d %d" % (A, B))
