import sys

def solution():
    input = sys.stdin.readline
    s = input().strip()
    a = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
    sum_alphabet = 0

    for alpha in s:
        sum_alphabet += a[ord(alpha) - 65]

    if sum_alphabet % 2 == 0:
        print("You're the winner?")
    else:
        print("I'm a winner!")
        
if __name__=='__main__':
    solution()
