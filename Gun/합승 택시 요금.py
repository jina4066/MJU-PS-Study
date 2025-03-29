import heapq

def solution(n, s, a, b, fares):
    answer = []
    inf = int(1e9)
    graph = [[] for _ in range(n + 1)]
    
    for start, end, dist in fares:
        graph[start].append((end, dist))
        graph[end].append((start, dist))
    

    def dijkstra(start, distance):
        q = [(0, start)]
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for node, fare in graph[now]:
                if dist + fare < distance[node]:
                    distance[node] = dist + fare
                    heapq.heappush(q, (dist + fare, node))
    
    distance = [inf] * (n + 1)
    dijkstra(s, distance)
    distance[s] += distance[a] + distance[b]
    
    for node in range(1, n + 1):
        if node == s:
            continue
            
        elif node in (a, b):
            new_distance = [inf] * (n + 1)
            dijkstra(node, new_distance)
            
            if node == a:
                distance[node] += new_distance[b]
            else:
                distance[node] += new_distance[a]
                
        else:
            new_distance = [inf] * (n + 1)
            dijkstra(node, new_distance)
            distance[node] += new_distance[a] + new_distance[b]

        
    return min(distance)
