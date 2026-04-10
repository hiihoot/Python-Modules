from typing import Callable

test_values = [16, 17, 16]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def spell(target: str, power: int) -> str:
    return f"{target} got hit, attack: {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(spell1, spell2):
        res1 = spell1("Dragon", 1)
        res2 = spell2("Dragon")
        return (res1, res2)
    return combiner(spell1, spell2)[1]


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def power_it(base_spell, multiplier):
        pass

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass

