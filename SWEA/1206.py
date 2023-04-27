T = 10

for test_case in range(1, T + 1):
  n = int(input())
  height = list(map(int, input().split()))
  
  cha = [-2, -1, 1, 2]
  result = 0
  
  for i in range(2, n - 2):
    cha_list = []
    for j in cha:
      cha_list.append(height[i + j])
      
    if height[i] <= max(cha_list):
      continue
    else:
      result += height[i] - max(cha_list)
      
  print("#%d %d" % (test_case, result))
