T = 10

for test_case in range(1, T + 1):
  tc = int(input())
  arr = [list(map(int, input().split())) for _ in range(100)]
  
  maxHap = 0    # 최대 합
  temp = 0
  temp1 = 0
  
  # 행과 열 계산
  for i in range(len(arr)):
    for j in range(len(arr)):
      temp += arr[i][j]    # 행의 합 계산
      temp1 += arr[j][i]   # 열의 합 계산
    if temp > maxHap:
      maxHap = temp     # 행의 합이 최대 합보다 크면 갱신
    if temp1 > maxHap:
      maxHap = temp1    # 열의 합이 최대 합보다 크면 갱신
    temp = 0
    temp1 = 0
  
  # 대각선 계산
  for i in range(len(arr)):
    for j in range(len(arr) - 1, -1, -1):
      temp += arr[i][j]
    if temp > maxHap:
      maxHap = temp
    temp = 0
    
  for i in range(len(arr)):
    temp += arr[i][i]
    
  if temp > maxHap:
    maxHap = temp
    
  print("#{} {}".format(tc, maxHap))
