'''
    Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized. 
    
    Examples 
    "the-stealth-warrior" gets converted to "theStealthWarrior" 
    
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior" 
    
    "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
'''


def to_camel_case(text: str) -> str:
    return ''.join([item.capitalize() if i != 0 else item for i, item in enumerate(text.split('-') if '-' in text else text.split('_'))]) if text else ''

assert to_camel_case("") == "" 
assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
assert to_camel_case("A-B-C") == "ABC"