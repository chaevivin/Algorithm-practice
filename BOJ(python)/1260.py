import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n + 1) for i in range(n + 1)]  # 노드 연결 여부를 False로 초기화

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = True  # 해당 노드들끼리 연결되어 있으면 True로 바꾸기

#print(graph)

visitedDfs = [False] * (n + 1)  # 방문 여부
visitedBfs = [False] * (n + 1)

def dfs(v, visited):
  visited[v] = True  # 해당 인덱스 값 방문 처리
  print(v, end=' ')

  for i in range(1, n + 1):
    if not visited[i] and graph[v][i]:  # 만약 i를 방문하지 않았고, 해당 인덱스와 연결 되어 있다면
      dfs(i, visited)  # 재귀

def bfs(v, visited):
  queue = deque([v])
  visited[v] = True  # 해당 인덱스 값 방문 처리

  while queue:  # 큐에 데이터가 없을 때가지 반복
    v = queue.popleft()  # 첫번째 값 꺼낸다
    print(v, end = ' ')

    for i in range(1, n + 1):
      if not visited[i] and graph[v][i]:  # 만약 i를 방문하지 않았고, 해당 인덱스와 연결 되어 있다면
        queue.append(i)  # i값을 큐에 추가
        visited[i] = True  # i값을 방문처리

dfs(v, visitedDfs)
print()
bfs(v, visitedBfs)
