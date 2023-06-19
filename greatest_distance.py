'''
The goal of this Kata is to return the greatest distance of index positions between matching number values in an array or 0 if there are no matching values.

Example: In an array with the values [0, 2, 1, 2, 4, 1] the greatest index distance is between the matching '1' values at index 2 and 5. Executing greatestDistance against this array would return 3. (i.e. 5 - 2)

Here's the previous example in test form:

assert greatest_distance([0, 2, 1, 2, 4, 1]), 3)
This is based on a Kata I had completed only to realize I has misread the instructions. I enjoyed solving the problem I thought it was asking me to complete so I thought I'd add a new Kata for others to enjoy. There are no tricks in this one, good luck!
'''
def greatest_distance(arr: list) -> int:
    res = 0
    for i, item_i in enumerate(arr):
        for j, item_j in enumerate(arr):
            if res < abs(i - j) and item_i == item_j:
                res = abs(i - j)
    return res



# greatest_distance([0,7,0,2,3,7,0,-1,-2])
assert greatest_distance([9, 7, 1, 2, 3, 7, 0, -1, -2]) == 4
assert greatest_distance([0,7,0,2,3,7,0,-1,-2]) == 6
assert greatest_distance([1,2,3,4]) == 0