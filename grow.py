

'''
    Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

    [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''
def grow(arr: list) -> int:
    return eval('*'.join([f'{item}' for item in arr]))

assert grow([1, 2, 3]) == 6
assert grow([4, 1, 1, 1, 4]) == 16
assert grow([2, 2, 2, 2, 2, 2]) == 64
