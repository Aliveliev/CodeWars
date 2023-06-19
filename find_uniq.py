'''
    There is an array with some numbers. All numbers are equal except for one. Try to find it!

    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    It’s guaranteed that array contains at least 3 numbers.

    The tests contain some very huge arrays, so think about performance.

    This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique
'''
from collections import Counter
def find_uniq(arr):
    return sorted(dict(Counter(arr)), key=lambda x: x, reverse=True)[0]

assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10