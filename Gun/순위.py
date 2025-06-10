def solution(n, results):
    answer = 0
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    
    for winner, loser in results:
        win[winner].append(loser)
        lose[loser].append(winner)
        
    def dfs(start, graph, visited):
        for node in graph[start]:
            if not visited[node]:
                visited[node] = True
                dfs(node, graph, visited)
        
    for i in range(1, n + 1):
        win_visited = [False] * (n + 1)
        dfs(i, win, win_visited)
        lose_visited = [False] * (n + 1)
        dfs(i, lose, lose_visited)

        if win_visited[1:].count(True) + lose_visited[1:].count(True) == n - 1:
            answer += 1
    
    return answer