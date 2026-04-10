from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} barrier"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool], spell: Callable) -> Callable:
    def guarded_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return guarded_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence_spell


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", ", ".join(combined("Dragon", 50)))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Goblin", 10))
    print("Amplified:", mega_fireball("Goblin", 10))

    print("\nTesting conditional caster...")
    strong_only = lambda t, p: p > 20
    powerful_heal = conditional_caster(strong_only, heal)
    print("Weak heal:", powerful_heal("Knight", 10))
    print("Strong heal:", powerful_heal("Knight", 25))

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, shield, heal])
    results = combo("Hero", 40)
    for result in results:
        print(">", result)   