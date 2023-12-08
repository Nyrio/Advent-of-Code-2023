import re
import typing

# Some utils from https://github.com/mcpower/adventofcode

def lmap(func, *iterables):
    return list(map(func, *iterables))

def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))