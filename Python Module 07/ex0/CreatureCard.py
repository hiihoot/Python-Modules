from Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str,
        cost: int, rarity: str,
        attack: int, health: int
            ):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"
        self.mana = 8

    def get_card_info(self):
        return {
                'name': self.name, 'cost': self.cost,
                'rarity': self.rarity, 'type': self.type,
                'attack': self.attack, 'health': self.health
               }

    def play(self, game_state: dict) -> dict:
        if self.is_playable(self.mana):
            self.mana -= self.cost
            return game_state

    def attack_target(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
