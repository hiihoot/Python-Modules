

class SpellCard():
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type
        self.mana = 6

    def play(self, game_state: dict) -> dict:
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        pass
