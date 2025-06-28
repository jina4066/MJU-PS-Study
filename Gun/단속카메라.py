def solution(routes):
    camera_cnt, car_idx = 0, 0
    routes.sort(key=lambda x: x[1])
    
    while car_idx < len(routes):
        camera_idx = routes[car_idx][1]
        camera_cnt += 1
        
        while True:
            car_idx += 1
            if car_idx >= len(routes):
                return camera_cnt
    
            if camera_idx < routes[car_idx][0] or routes[car_idx][1] < camera_idx:
                break
            
    return camera_cnt