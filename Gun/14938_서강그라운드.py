import sys, heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(r):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
max_item = 0

for start in range(1, n + 1):
    distance = [INF] * (n + 1)   
    q = [(0,start)]
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))
    
    item = 0
    
    for i in range(1, n + 1):
        if distance[i] <= m:
            item += items[i - 1]

    max_item = max(max_item, item)
    
print(max_item)
