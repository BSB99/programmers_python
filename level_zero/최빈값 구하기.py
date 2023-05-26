def solution(array):
    storage = {}
    arr = []
    num = 0
    
    for i in array:
        storage.setdefault(i, 0)
        storage[i] += 1
    
    print(storage)
    
    for i in storage:
        arr.append(storage[i])
    
    
    
    max_num = max(arr)
    
    for i in arr:
        if i == max_num:
            num += 1
            
    if num > 1:
        return -1
    
    return [k for k, v in storage.items() if v == max_num][0]

print(solution([1, 2, 3, 3, 3, 4])) # 3