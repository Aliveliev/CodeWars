'''
    Binary with unknown bits:
    You received a string of a binary number, but there are some x in it. It cannot be used, so the solution is to get the average of all possible numbers.

    Rule:
    The string consists of 0, 1 and x, if it has 2 or more bits, it would have at least one x.

    Unless the number is a single zero(0), otherwise no leading zeros would occur, you don't need to worry about invalid input.

    x can be 0 or 1, but it has to follow the 2nd rule above.

    You need to return the average number of all possible numbers following the above rule. As it may be a float, the difference should be less than 0.01.

    Performance:
    The length of input binary string would be less or equal to 50.

    It may consist up to 30 x, so the approach of listing out all possible numbers would time out.

    Examples:
    Here are some examples:

    binary = 'x'
    possible: '0', '1' => 0, 1
    average = 0.5


    binary = 'x0'
    possible: '10' => 2 ('00' violated the rule)
    average = 2

    binary = '1x0x'
    possible: '1000', '1001', '1100', '1101' => 8, 9, 12, 13
    average = 10.5

    other sample tests:
    '0' => 0
    '1' => 1
    '1x' => 2.5
    'xx' => 2.5
    '1x0' => 5
    '1xxx1xxx0xxx0xxx1xxx1xxx0xxx0xxx1xxx0' => 105084647303
'''
def binary_average(binary: str) -> int:
    # res = ['']
    # for ch in binary:
    #     if ch == 'x':
    #         res = [item + '0' for item in res] + [item + '1' for item in res]
    #     else:
    #         res = [item + ch for item in res]

    # res = [int(item, 2) for item in res if item[0] != '0' or item == '0']
    # return sum(res) / len(res)
    x_count = binary.count('x')
    if x_count == 0:
        return int(binary, 2)
    total = 0
    for bit in ['0', '1']:
        new_binary = binary.replace('x', bit, 1)
        if new_binary[0] != '0' or new_binary == '0':
            total += binary_average(new_binary)
    return total / (2 ** x_count)

assert binary_average('x') == 0.5
assert binary_average('0') == 0
assert binary_average('1') == 1
assert binary_average('1x') == 2.5
assert binary_average('x0') == 2
assert binary_average('xx') == 2.5
assert binary_average('1x0') == 5
assert binary_average('1x0x') == 10.5
assert binary_average('1xxx1xxx0xxx0xxx1xxx1xxx0xxx0xxx1xxx0') == 105084647303
