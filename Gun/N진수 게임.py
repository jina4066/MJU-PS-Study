def div(n, base):
    if n == 0:
        return '0'
    digits = '0123456789ABCDEF'
    result = ''
    while n > 0:
        n, mod = divmod(n, base)      
        result = digits[mod] + result
    
    return result

def solution(n, t, m, p):
    answer = ''
    for i in range(t*m):
        answer += div(i, n)
        
    return answer[p-1::m][:t]
