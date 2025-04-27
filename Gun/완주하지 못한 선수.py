# Sol.1
from collections import Counter
def solution(p, c):
    return "".join(Counter(p) - Counter(c))

# Sol.2
def solution(p, c):
    dic = {}
    temp = 0
    for part in p:
        dic[hash(part)] = part
        temp += hash(part)
    for com in c:
        temp -= hash(com)
    
    return dic[temp]