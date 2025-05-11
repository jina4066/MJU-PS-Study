import math

def solution(arr):
    lcm = min(arr)
    for num in sorted(arr):
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm