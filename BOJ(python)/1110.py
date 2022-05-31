import sys

N = int(sys.stdin.readline())
new_N = 0
cnt = 0

if N == 0:
  cnt = 1

while new_N != N:
  if cnt == 0:
    N_1 = N % 10
    N_10 = N // 10
  else:
    N_1 = new_N % 10
    N_10 = new_N // 10
  new_N = (N_1 + N_10) % 10 + N_1 * 10
  cnt += 1
  
print(cnt)
