from itertools import product

def solution(word):
    word = list(word)
    
    alphabets = ['A', 'E', 'I', 'O', 'U']
    a = []
    
    for i in range(1,6):
        for j in product(alphabets, repeat=i):
            a.append(list(j))
    
    return sorted(a).index(word) + 1
