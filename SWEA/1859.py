T = int(input())

for test_case in (1, T + 1):
  n = int(input())
  price = list(map(int, input().split()))
  
  result = 0
  max_price = 0
  
  for i in range(len(price) - 1, -1, -1):
    if max_price < price[i]:
      max_price = price[i]
    else:
      result += max_price[i] - price[i]
      
  print("#%d %d" % (test_case, result))
