def solution(rank, attendance):
    data = []
    result = []
    
    for i in range(len(attendance)):
        if (attendance[i]):
            data.append(rank[i])  
    
    data.sort()
    
    for j in range(3):
        result.append(rank.index(data[j]))
    
    a, b, c = result[:3]
    
    return 10000 * a + 100 * b + c
