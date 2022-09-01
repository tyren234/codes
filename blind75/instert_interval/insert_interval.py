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
        i = len(intervals) - 1
        while i >= 0:
            if intervals[i][1] < newInterval[0]:
                # wstawianie po prawej itego interwalu
                new = []
                
            i -= 1

print(insert([[1,3],[6,9]], [-1,0]))