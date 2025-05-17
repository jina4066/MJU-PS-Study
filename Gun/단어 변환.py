# Sol1. DFS

def solution(begin, target, words):
    answer = len(words)

    if target not in words:
        return 0
    
    def is_matched(w1, w2):
        return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1
    
    visited = set()
    
    def dfs(depth, word):
        nonlocal answer
        
        if word == target:
            answer = min(answer, depth)
            return
         
        for next_word in words:
            if next_word not in visited and is_matched(next_word, word):
                visited.add(next_word)
                dfs(depth + 1, next_word)
                visited.remove(next_word)
        
    dfs(0, begin)
    
    return answer


# Sol2. BFS

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def is_matched(w1, w2):
        return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1
    
    visited = set()
    queue = deque([(begin, 0)])
    
    while queue:
        cur, depth = queue.popleft()
        
        if cur == target:
            return depth
        
        for next_word in words:
            if next_word not in visited and is_matched(next_word, cur):
                visited.add(next_word)
                queue.append((next_word, depth + 1))
    
    return 0