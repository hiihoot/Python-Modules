from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul, max as op_max, min as op_min
from typing import Callable, Any, Dict, List

def spell_reducer(spells: List[int], operation: str) -> int:
    """
    Reduce a list of spell powers using the specified operation.
    Supports: 'add', 'multiply', 'max', 'min'
    Returns 0 for empty spells.
    """
    if not spells:
        return 0

    ops: Dict[str, Callable] = {
        "add": add,
        "multiply": mul,
        "max": op_max,
        "min": op_min
    }

    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")

    # For max/min with single element, reduce needs initializer
    if operation in ("max", "min"):
        return reduce(ops[operation], spells)
    else:
        return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> Dict[str, Callable]:
    """
    Create specialized enchantment functions by pre-filling power=50 and element.
    Returns a dictionary of partial functions.
    """
    fire_enchant = partial(base_enchantment, 50, "fire")
    water_enchant = partial(base_enchantment, 50, "water")
    earth_enchant = partial(base_enchantment, 50, "earth")

    return {
        "fire": fire_enchant,
        "water": water_enchant,
        "earth": earth_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number with memoization.
    Uses lru_cache to cache results and improve performance.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher() -> Callable[[Any], str]:
    """
    Base dispatcher for spells. Will be overridden by registered types.
    """
    def _handler(arg):
        return "Unknown spell type"
    return _handler


@spell_dispatcher.register
def _(arg: int) -> str:
    return f"Damage spell: {arg} damage"


@spell_dispatcher.register
def _(arg: str) -> str:
    return f"Enchantment: {arg}"


@spell_dispatcher.register
def _(arg: list) -> str:
    return f"Multi-cast: {len(arg)} spells"


# --- Testing Code ---
if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # Uncomment to see cache stats: print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))

    # Test partial_enchanter
    def sample_enchant(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} enchantment of power {power} on {target}"
    
    enchanters = partial_enchanter(sample_enchant)
    print(f"Fire on dragon: {enchanters['fire']('dragon')}")
    print(f"Water on knight: {enchanters['water']('knight')}")   