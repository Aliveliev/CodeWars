'''
    In elementary arithmetic a "carry" is a digit that is transferred from one column of digits to another column of more significant digits during a calculation algorithm.

    This Kata is about determining the number of carries performed during the addition of multi-digit numbers.

    You will receive an input string containing a set of pairs of numbers formatted as follows:

    123 456
    555 555
    123 594
    And your output should be a string formatted as follows:

    No carry operation
    3 carry operations
    1 carry operations
    Some Assumptions
    Assume that numbers can be of any length.
    But both numbers in the pair will be of the same length.
    Although not all the numbers in the set need to be of the same length.
    If a number is shorter, it will be zero-padded.
    The input may contain any arbitrary number of pairs.
'''
def solve(input_string):
    pass

assert solve("123 456\n555 555\n123 594") == "No carry operation\n3 carry operations\n1 carry operations"
assert solve("321 679\n098 805\n123 867") == "3 carry operations\n2 carry operations\n1 carry operations"
assert solve("123 457\n631 372\n999 111") == "1 carry operations\n2 carry operations\n3 carry operations"
assert solve("123 457\n123 456\n654 312\n999 000\n123 457") == "1 carry operations\nNo carry operation\nNo carry operation\nNo carry operation\n1 carry operations"
assert solve("1 9\n123456789 111111101\n01 09\n11 09\n123 457") == "1 carry operations\n1 carry operations\n1 carry operations\n1 carry operations\n1 carry operations"
assert solve("99 99") == "2 carry operations"