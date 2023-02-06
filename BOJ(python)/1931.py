import sys

n = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

time.sort(key = lambda x: (x[1], x[0]))
print(time)

count = 1
end_time = time[0][1]

for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)
