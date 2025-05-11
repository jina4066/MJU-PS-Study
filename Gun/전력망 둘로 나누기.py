from collections import deque

def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue

            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        # count the nodes
        visited = [0] * (n + 1)

        # find the first node
        start = 0
        for node in graph:
            if node:
                start = node[0]
                break

        q = deque([start])

        while q:
            node = q.popleft()

            if not visited[node]:
                visited[node] = 1
                q.extend(graph[node])

        count = abs(n - 2 * sum(visited))
        answer = min(answer, count)

    return answer