# check if the string is right 
d = {
    ")": "(",
    "}": "{",
    "]": "["
}

def check(ss):
    global d
    stack = []
    # pop if the next stirng is: ( -> ), [ -> ], { -> }
    for i in range(len(ss)):      
        if ss[i] in d.values():
            stack.append(ss[i])
            
        else:
            if stack and stack[-1] == d[ss[i]]:
                stack.pop()
            else:
                stack.append(ss[i])

    return True if not stack else False
    
    
def solution(s):    
    # spin string -> string * 2 and iterate 0:6, 1:7 ... 5:11
    count = 0
    ss = s * 2
    size = len(s)
    a = []
    for i in range(size):      
        if check(ss[i:i+size]):
            count += 1
    
    return count
