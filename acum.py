'''
    accum("abcd") -> "A-Bb-Ccc-Dddd" 
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy" 
    accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

def accum(text: str) -> str:
    return '-'.join([f'{item*i}'.capitalize() for i, item in enumerate(text, 1)])

assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy" 
assert accum("cwAt") == "C-Ww-Aaa-Tttt"
assert accum("Veliev") == "V-Ee-Lll-Iiii-Eeeee-Vvvvvv"