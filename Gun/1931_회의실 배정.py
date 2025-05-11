import sys
input = sys.stdin.readline

n = int(input())
meetings = []
cnt = 1

for _ in range(n):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key=lambda x: [x[1], x[0]])
first = meetings[0]
end = first[1]

for meeting in meetings[1:]:
    next_start, next_end = meeting
    if end <= next_start:
        cnt += 1
        end = next_end

print(cnt)