# Sol1. kruskal

def solution(n, costs):
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        root_a, root_b = find(a), find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False
    
    costs.sort(key=lambda x: x[2])
    total = 0
    
    for a, b, cost in costs:
        if union(a, b):
            total += cost
    
    return total

# Sol2. prim

import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    
    # 양방향 그래프 구성
    for u, v, cost in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, start_node)
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for edge_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_cost, v))
    
    return total_cost