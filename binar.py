def binar(l: list) -> int:
    return int(''.join([str(item) for item in l]), 2)

assert binar([0, 0, 0, 1]) == 1
assert binar([0, 0, 1, 0]) == 2
assert binar([0, 1, 0, 1]) == 5
assert binar([1, 0, 0, 1]) == 9
assert binar([0, 0, 1, 0]) == 2
assert binar([0, 1, 1, 0]) == 6
assert binar([1, 1, 1, 1]) == 15
assert binar([1, 0, 1, 1]) == 11