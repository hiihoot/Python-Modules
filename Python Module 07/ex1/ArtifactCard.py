
class ArtifactCard:
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        self.name = name
        self.cost = cost
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass
