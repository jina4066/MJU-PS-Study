import sys

def solution():
    input = sys.stdin.readline
    n = int(input())

    for _ in range(n):
        answer = 2
        word = input().strip()

        if word == word[::-1]:
            answer = 0
        else:
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    new1 = word[i + 1:j + 1]
                    new2 = word[i:j]
                    if new1 == new1[::-1] or new2 == new2[::-1]:
                        answer = 1
                    break
                i += 1
                j -= 1
        print(answer)
    
if __name__=='__main__':
    solution()
