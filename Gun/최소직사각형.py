def solution(sizes):
    # sort the sizes
    max1, max2 = 0, 0
    
    # find the max in size[0], size[1]
    for size in sizes:
        size.sort()
        max1 = max(size[0], max1)
        max2 = max(size[1], max2)
    
    return max1 * max2