import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

gop = A * B * C
gop = str(gop)

num = []
for i in gop:
    num.append(i)

cnt = [0 for i in range(10)]
for i in num:
  if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
    cnt[int(i)] += 1

for i in cnt:
    print(i)
