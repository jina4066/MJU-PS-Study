# Sol1. combinations

from itertools import product

def solution(user_id, banned_id):
    answer = set()
    id_holder = [] 

    for id in banned_id:
        possible_ids = [
            user for user in user_id 
            if len(user) == len(id) and 
            all(i == "*" or i == u for i, u in zip(id, user))
        ]
        
        id_holder.append(possible_ids)
        
    for ids in product(*id_holder):
        if len(set(ids)) == len(banned_id):
            answer.add(frozenset(list(ids)))

    return len(answer)

# Sol2. DFS + Backtracking

def solution(user_id, banned_id):
    id_holder = [] 
    
    for id in banned_id:
        possible_ids = [
            user for user in user_id 
            if len(user) == len(id) and 
            all(i == "*" or i == u for i, u in zip(id, user))
        ]     
        id_holder.append(possible_ids)
    
    result = set()
    
    def dfs(depth, path):
        if depth == len(banned_id):
            result.add(frozenset(path))
            return
        
        for user in id_holder[depth]:
            if user not in path:
                dfs(depth + 1, path + [user])
    
    dfs(0, [])
    
    return len(result)