import sys

def solution():
    input = sys.stdin.readline

    while (s := input().strip()) != 'end':
        wl = ['e', 'o']
        mo = ['a', 'e', 'i', 'o', 'u']
        is_mo, illegal = False, False
        mo_cnt, ja_cnt = 0, 0

        if s[0] in mo:
            is_mo = True
            mo_cnt += 1
        else:
            ja_cnt += 1

        for i in range(1, len(s)):
            v = s[i]

            if v in mo:
                mo_cnt += 1
                is_mo = True
                ja_cnt = 0
            else:
                mo_cnt = 0
                ja_cnt += 1

            if v not in wl and v == s[i - 1]:
                illegal = True
                break

            if mo_cnt >= 3 or ja_cnt >= 3:
                illegal = True
                break
                
        if not is_mo or illegal:
            print(f"<{s}> is not acceptable.")
        else:
            print(f"<{s}> is acceptable.")

if __name__ == '__main__':
    solution()