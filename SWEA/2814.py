def dfs(v, cnt):
  global answer
  
  if cnt > answer:
    answer = cnt    # cnt가 1 증가할 때마다 answer 갱신
    
  for i in visited[v]:
    if not visited[i]:
      visited[i] = 1    # 방문처리 
      dfs(i, cnt + 1)
      visited[i] = 0    # 방문처리 취소 (모든 거리 검사)
      
for tc in range(1, int(input()) + 1):
  n, m = map(int, input().split())
  graph = [[] for _ in range(m + 1)]
  
  for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
  for i in range(1, n + 1):
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0
    
  print('#{} {}'.format(tc, answer))
