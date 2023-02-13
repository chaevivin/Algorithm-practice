import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# 한줄 입력 받고, 우측의 '\n' 제거한 후, 모든 원소를 int형으로 변환한 배열을 생성
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      # 갈 수 없는 경우 무시
      if graph[nx][ny] == 0:
        continue

      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록  
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1  # 누적 거리값
        queue.append((nx, ny))

  # 최단 거리 반환
  return graph[n - 1][m - 1]
    
print(bfs(0, 0))
