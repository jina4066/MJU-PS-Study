# Sol 1. O(n^2)

def solution(lines):
    answer = 0
    timeline, timerange = [], []
    
    for line in lines:
        a, b, c = line.split()
        h, m, s = b.split(":")
        end_time = int(1000 * (int(h) * 3600 + int(m) * 60 + float(s)))
        t = int(1000 * float(c[:-1]))
        start_time = end_time - t + 1
        
        timeline.append(end_time)
        timerange.append((start_time, end_time))
        
    for i in sorted(timeline):
        cnt = 0
        for s, e in timerange:
            if i + 999 >= s and i <= e:
                cnt += 1
        answer = max(answer, cnt)
        
    return answer


# Sol 2. 더러운 코드와 성능 개선 - 탐색 범위를 end_time으로만 관리하여 연산 횟수 1/2로 줄이기

def solution(lines):
    timeline, timerange = [], []
    
    for line in lines:
        _, end_str, duration_str = line.split()
        h, m, s = end_str.split(":")
        sec, ms = s.split(".")
        end_time = (int(h) * 3600 + int(m) * 60 + int(sec)) * 1000 + int(ms)
        duration = int(1000 * float(duration_str[:-1]))
        start_time = end_time - duration + 1
        
        timeline.append(end_time)
        timerange.append((start_time, end_time))
    
    answer = 0
    
    for point in timeline:
        w_start, w_end = point, point + 999
        count = sum(1 for s, e in timerange if s <= w_end and e >= w_start)
        answer = max(answer, count)
        
    return answer