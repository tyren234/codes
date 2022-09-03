def insert(intervals : 'list[list[int]]', newInterval : 'list[int]') -> 'list[list[int]]':
    result = []
    if intervals[0][0] > newInterval[1]: 
        result.append(newInterval)
        result.extend(intervals)
        return result
    elif intervals[-1][1] < newInterval[0]:
        result.extend(intervals)
        result.append(intervals)
        return result
    else:
        for n,i in enumerate(intervals):
            if  i[0] <= newInterval[1] and i[1] >= newInterval[0]: #intervals overlapse
                    newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
                    result = intervals[:n]
                    print(result)
                    result.append(newInterval)
                    print(result)
                    if n != len(intervals):
                        result.extend(intervals[n+1:])
                        print(result)
                    print()
    return result
                    


 # 7 - 8
 # 1 - 3, 4 - 5, 9 - 10, 14 - 16

print(insert([[1,3],[6,9]],[2,7]))