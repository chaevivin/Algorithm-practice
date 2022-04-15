import sys

a, b, c = map(int, sys.stdin.readline().split())
price = 0

if a == b and b == c:
	price = 10000 + a * 1000
elif a == b or b == c or a == c: 
	if a == b:
		price = 1000 + a * 100
	if b == c:
		price = 1000 + b * 100
	if a == c:
		price = 1000 + c * 100
else:
	price = max(a, b, c) * 100

print(price)
