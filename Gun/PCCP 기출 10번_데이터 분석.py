def solution(data, ext, val_ext, sort_by):
    filter = ["code", "date", "maximum", "remain"]
    ext_idx = 0
    sort_idx = 0
    
    for i in range(4):
        if ext == filter[i]:
            ext_idx = i
        if sort_by == filter[i]:
            sort_idx = i
            
    new = []
    for d in data:
        if d[ext_idx] < val_ext:
            new.append(d)
    answer = sorted(new, key=lambda x: x[sort_idx])
    return answer
