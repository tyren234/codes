# This problem can be simplified to the Fibonacci sequence 
# Starting from the last step (let's say n = 5)
# ====== ====== ====== ====== ====== ======
# | x  | | x  | | x  | | x  | | x  | | x  |
# ====== ====== ====== ====== ====== ======
#   0       1     2       3      4      5
# Then, in how many ways can we reach the end if we are on index 4?
# The answer is one. One way only - making one step up.
# Now in how many ways can we reach the end if we are on index 5?
# This is the edge case - last element. What happens if our staircase has only one step?
# Well, we can be at the top in one step.
# At this moment we can fill two spots: indeces 4 and 5:
# ====== ====== ====== ====== ====== ======
# | x  | | x  | | x  | | x  | |  1 | |  1 |
# ====== ====== ====== ====== ====== ======
# Knowing this, it's only natural that every following x should equal the sum of two previous,
# since we can either go to the next or to the second next step and we have already computed the
# number of ways we can finish when we land on these steps.
# Filled array would look like this:
# ====== ====== ====== ====== ====== ======
# | 8  | | 5  | | 3  | | 2  | | 1  | | 1  |
# ====== ====== ====== ====== ====== ======
# Furthermore we can even get rid of the array and store only two previous elements and such solution is written below.


def climbing_stairs(n:int)->int:
    a, b = 1, 1
    for i in range(n-1):
        temp = a
        a = a + b
        b = temp
    return a