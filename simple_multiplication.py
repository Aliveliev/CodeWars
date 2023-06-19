'''
    This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
'''
def simple_multiplication(item: int) -> int:
    return item * 8 if item % 2 == 0 else item * 9  

assert simple_multiplication(2) == 16
assert simple_multiplication(1) ==  9
assert simple_multiplication(8) == 64
assert simple_multiplication(4) == 32
assert simple_multiplication(5) == 45