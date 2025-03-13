def solution(s):
    a = sorted(s[2:len(s) - 2].split("},{"), key=len)
    b = []

    for i in range(len(a)):
        v = []
        for j in a[i].split(","):
            v.append(int(j))
        b.append(v)

    answer = b[0]

    for i in range(1, len(a)):
        v = set(b[i]) - set(answer)
        answer = answer + list(v)

    return answer
