'''
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_'). 
    
    Examples: 
    
    * 'abc' =>  ['ab', 'c_'] 
    * 'abcdef' => ['ab', 'cd', 'ef']
'''


def pair(text: str) -> list:
    return [f'{text[i:i+2]}_' if len(text[i:i+2]) == 1 else f'{text[i:i+2]}' for i in range(0, len(text), 2)]

assert pair('abc') == ['ab', 'c_'] 
assert pair('abcdef') == ['ab', 'cd', 'ef']
