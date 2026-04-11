import time
from typing import Callable, Any
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = kwargs.get('power')
            if power is None:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break

            # Validate power
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"({attempt}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# --- Test Execution Block ---
if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("Testing retrying spell...")

    # Simulating a failing spell
    fail_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell():
        global fail_count
        fail_count += 1
        if fail_count <= 3:
            raise ValueError("Fizzle!")
        return "Spell worked!"

    print(unstable_spell())

    # Simulating a successful spell on the first try
    @retry_spell(max_attempts=3)
    def waaagh_spell():
        return "Waaaaaaagh spelled !"

    print(waaagh_spell())

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("True Mage"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Frostbolt", 5))
