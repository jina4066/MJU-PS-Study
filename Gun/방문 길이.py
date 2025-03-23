
def solution(dirs):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    d = {
        "U":2,
        "D":3,
        "L":1,
        "R":0
    }
    points = []
    start = (0, 0)
    
    for dir in dirs:
        idx = d[dir]
        x, y = start
        x += dx[idx]
        y += dy[idx]
        
        if abs(x) > 5 or abs(y) > 5:
            continue
        
        end = (x, y)
        points.append(tuple(sorted([start, end])))
        start = end
    
    return len(set(points))
            