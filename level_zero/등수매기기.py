def solution(score):
    result = []
    avg = []

    for i in score:
        avg.append(sum(i) / 2)

    sort_arr = sorted(avg, reverse = True)

    for i in avg:
        result.append(sort_arr.index(i) + 1)

    return result