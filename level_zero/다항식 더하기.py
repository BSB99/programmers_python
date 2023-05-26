def solution(p):
    array = p.split(' ')

    x = 0
    y = 0
    
    for i in array:
        if i != '+':
            if i == 'x':
                x += 1   
            elif 'x' in i:
                x += int(i[:-1])
            else:
                y += int(i)
                
    if x == 1 and y > 0:
        return 'x + {0}'.format(y)            
    elif x == 1:
        return 'x'
    elif y == 0:
        return '{0}x'.format(x)
    elif x == 0:
        return '{0}'.format(y)
    else:
        return '{0}x + {1}'.format(x, y)