from functools import reduce, partial
from typing import Callable, Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    valid_operations = ["add", "multiply", "max", "min"]

    if not spells:
        return 0
    
    if not operation in valid_operations:
        raise ValueError("Invalid operation")
    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "multiply":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    if operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    
    

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "water": partial(base_enchantment, power=50, element="water"),
        "wood": partial(base_enchantment, power=50, element="wood")
    }


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    pass
