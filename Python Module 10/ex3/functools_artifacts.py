from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any, Dict, List


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0

    ops: Dict[str, Callable | None] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    func = ops.get(operation)
    if func:
        return reduce(func, spells)
    return 0


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> Dict[str, Callable]:
    fire_enchant = partial(base_enchantment, 50, "fire")
    water_enchant = partial(base_enchantment, 50, "water")
    earth_enchant = partial(base_enchantment, 50, "earth")

    return {
        "fire": fire_enchant,
        "water": water_enchant,
        "earth": earth_enchant,
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg: Any):
        return "Unknown spell type"

    @spell.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return spell


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
    print(dispatcher(2.3))

    # Test partial_enchanter
    def sample_enchant(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} \
            enchantment of power" f"{power} on {target}"

    enchanters = partial_enchanter(sample_enchant)
    print(f"Fire on dragon: {enchanters['fire']('dragon')}")
    print(f"Water on knight: {enchanters['water']('knight')}")
