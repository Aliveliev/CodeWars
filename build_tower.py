'''
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''
def tower_builder(n_floors: int) -> list:
    return [f'{" " * (n_floors - n - 1)}{"*" * (n * 2 + 1)}{" " * (n_floors - n - 1)}' for n in range(n_floors)]

assert tower_builder(1) == ['*', ]
assert tower_builder(2) == [' * ', '***']
assert tower_builder(3) == ['  *  ', ' *** ', '*****']
