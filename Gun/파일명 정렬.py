def solution(files):
    names = []
    
    for file in files:
        head, number, tail = "", "", ""
        number_start, number_end = False, False
    
        for c in file:
            if c.isdigit():
                if not number_end:
                    number_start = True
                    number += c
                else:
                    tail += c
            else: 
                if not number_start:
                    head += c
                else:
                    number_end = True
                    tail += c
        
        names.append([head, number, tail])
         
    return ["".join(name) for name in sorted(names, key=lambda x: [x[0].upper(), int(x[1])])]
    
# Sol2.
import re 

def solution2(files):
    a = sorted(files, key=lambda file: int(re.findall(r'\d{1,5}', file)[0]))
    return sorted(a, key=lambda file: re.split(r'\d{1,5}', file.upper())[0])
