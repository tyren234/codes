def merge(left: list[int], right: list[int]) -> list[int]:
    l = 0
    r = 0
    output = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
    # notice that l or r is equal to len(left) or len(right), so they will not add anything
    output += left[l:]
    output += right[r:]
    return output

def merge_sort(array: list[int]) -> list[int]:
    if len(array) in [0, 1]:
        return array
    mid = len(array)//2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

# unsorted = [1,2,789,23,5,95,8,28,5,782,7,2598,6,49,816,84,6519,81,94,984,984,65,489,19,849,49,49,46,46,849,49,5,6,52,16,19,987,94,32,198]
unsorted = [100000,2,35,4,89,79,632,16,84,6,219,81,981,98,1,968,498,7,1,65,16,65,16,5,98,7,7,897,897,94,65,431,3,12,65,46,54,987,65,63,8,96,516,8,46,96849,0,9,191,981,9,8,9,00,9879,0,684,5]

output = merge_sort(unsorted)
print(output)