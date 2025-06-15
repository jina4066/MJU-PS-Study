def solution(words):
    trie = {}
    
    def insert(word):
        node = trie
        for char in word:
            if char not in node:
                node[char] = {'_count': 0}
            node = node[char]
            node['_count'] += 1
        node['#'] = True
        
    def auto_complete(word):
        node = trie
        length = 0
        for char in word:
            length += 1
            node = node[char]
            if node['_count'] == 1:
                break
        return length
    
    for word in words:
        insert(word)
                    
    return sum(auto_complete(word) for word in words)