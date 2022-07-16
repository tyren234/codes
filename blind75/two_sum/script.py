from typing import Dict

from black import target_version_option_callback


def two_sum(arr : list[int], target : int) -> int:
    seen = dict()   
    for i in range(len(arr)):
        if seen.get(target - arr[i]) == None:
            seen[arr[i]] = i
        else:
            return (seen.get(target - arr[i]), i)

# print(two_sum([2,7,11,15], 17))
