def change(nums, cnt):
  global result
  
  temp = ''
  for num in nums:
    temp += num
    
  if int(temp) in result[cnt]:
    return
  else:
    result[cnt].append(int(temp))
    
  if cnt == 0:
    return
  
  n = len(nums)
  for i in range(n):
    for j in range(1, n + 1):
      nums[i], nums[j] = nums[j], nums[i]
      change(nusm, cnt - 1)
      nums[i], nums[j] = nums[j], nums[i]
      
T = int(input())

for test_case in range(1, T + 1):
  temp, cnt = input().split()
  
  nums = list(temp)
  result = [[] for _ in range(int(cnt) + 1)]
  
  change(nums, cnt)
  
  print("#%d %d" % (test_case, max(result[0])))
