from itertools import product

def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]
    result = []
    for rates in product(discount, repeat=len(emoticons)):
        result = [0, 0]
        for rate, plus_price in users:
            cost = 0
            for i in range(len(rates)):
                if rate <= rates[i]:
                    cost += emoticons[i] * (100 - rates[i]) // 100
            
            if cost >= plus_price:
                result[0] += 1
            else:
                result[1] += cost
        
        answer.append(result)
                
    return sorted(answer)[-1]
