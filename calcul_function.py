def zero(ch: str = ""): return eval(f'0{ch}')
def one(ch: str = ""): return eval(f'1{ch}')
def two(ch: str = ""): return eval(f'2{ch}')
def three(ch: str = ""): return eval(f'3{ch}')
def four(ch: str = ""): return eval(f'4{ch}') 
def five(ch: str = ""): return eval(f'5{ch}')
def six(ch: str = ""): return eval(f'6{ch}')
def seven(ch: str = ""): return eval(f'7{ch}')
def eight(ch: str = ""): return eval( f'8{ch}')
def nine(ch: str = ""): return eval(f'9{ch}')

def plus(ch: str = ""): return f'+{ch}'
def minus(ch: str = ""): return f'-{ch}'
def times(ch: str = ""): return f'*{ch}'
def divided_by(ch: str = ""): return f'//{ch}'


assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3
