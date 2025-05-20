import sys
sys.setrecursionlimit(10**6)
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        nodes = computers[node]
        for i in range(n):
            if node != i and not visited[i] and nodes[i] == 1:
                dfs(i)
        return
    
    for node in range(n):
        if not visited[node]:
            answer += 1
            dfs(node)
            
    return answer
