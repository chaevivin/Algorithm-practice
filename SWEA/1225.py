T = 10

for test_case in range(1, T + 1):
  tc = int(input())
  data = list(map(int, input().split()))
  
  cnt = 1
  temp = 0
  
  while True:
    if cnt == 6:    # 한 사이클 1 ~ 5
      cnt = 1
      
    temp = data[0]
    for i in range(1, len(data)):    # 숫자 한 칸씩 앞으로 옮기기
      data[i - 1] = data[i]
    data[-1] = temp - cnt    # 마지막에는 첫 번째 숫자 - cnt
    
    if data[-1] <= 0:    # 마지막 숫자가 0이거나 음수면 무조건 0 그리고 break => 암호 생성
      data[-1] = 0
      break
      
    cnt += 1
      
  print("#{}".format(tc), end = ' ')
  for i in data:
    print("{}".format(i), end = ' ')
  print("")
