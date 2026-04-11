from functools import wraps
import time
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    """
    Decorator that measures and prints execution time of a function.
    Preserves original function metadata using wraps.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    """
    Parameterized decorator that validates the first argument (power)
    of the decorated function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power >= min_power:
                return func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:
    """
    Decorator that retries the function up to max_attempts times
    if it raises an exception.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
                        continue
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    """
    A class representing a guild of mages.
    """
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Static method to validate a mage name.
        Name must be at least 3 characters and contain only letters/spaces.
        """
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Cast a spell if power is sufficient.
        Uses power_validator decorator with min_power=10.
        """
        return f"Successfully cast {spell_name} with {power} power"

# --- Testing Code ---
if __name__ == "__main__":
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise Exception("Magic unstable!")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Weak Spark", 5))   