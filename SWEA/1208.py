T = 10

for test_case in  range(1, T + 1):
  dump = int(input())    # 덤프 횟수
  box_height = list(map(int, input().split()))    # 각 상자의 높이 리스트
  
  count = 0    # 현재 횟수
  while True:
    box_height.sort()
    
    if count == dump:
      break
    else:  
      # 덤프 실행
      box_height[0] += 1
      box_height[-1] -= 1
      count += 1
    
  result = box_height[-1] - box_height[0]
  
  print("#{} {}".format(test_case, result))
