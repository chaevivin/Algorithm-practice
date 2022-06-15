n, k = map(int, input().split())  
coin = [int(input()) for i in range(n)]
  
dp = [1] + [0 for _ in range(k)]
for i in coin:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])
