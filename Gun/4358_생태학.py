import sys
from collections import Counter

def solution():
    tree = Counter(sys.stdin.read().split("\n"))
    del tree[""]
    l = sum(tree.values())
    
    for name in sorted(tree.keys()):
            print("%s %.4f" % (name, tree[name] / l * 100))

if __name__=='__main__':
    solution()