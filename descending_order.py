'''
    Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

    Examples:
    Input: 42145 Output: 54421

    Input: 145263 Output: 654321

    Input: 123456789 Output: 987654321
'''
def descending_order(num: int) -> int:
    return int(''.join(sorted(str(num), reverse=True)))

assert descending_order(0) == 0
assert descending_order(15) == 51
assert descending_order(123456789) == 987654321