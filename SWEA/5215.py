def dfs(idx, sTaste, sKcal):
  global maxTaste
  
  if sKcal > L:    # 현재 칼로리가 제한 칼로리보다 높으면 return
    return
  
  if maxTaste < sTaste:    # 현재 점수가 maxTaste 점수보다 높으면 갱신
    maxTaste = sTaste

  if idx == N:    # 재료 리스트를 다 검사했으면 return
    return
  
  taste, kcal = data[idx] 
  
  dfs(idx + 1, sTaste + taste, sKcal + kcal)    # 재료 리스트에 있는 재료를 사용하는 경우
  dfs(idx + 1, sTaste, sKCal)    # 재료 리스트에 있는 재료를 사용하지 않는 경우 (다른 조합 사용 x)
    
T = int(input())

for test_case in range(1, T + 1):
  N, L = map(int, input().split())    # N : 재료의 수, L : 제한 칼로리
  data = [list(map(int, input().split())) for _ in range(N)]    # 재료의 점수와 칼로리를 담은 리스트
  
  maxTaste = 0
  dfs(0, 0, 0)
  
  print("#{} {}".format(test_case, maxTaste))
