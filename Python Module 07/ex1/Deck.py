from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards = {}
        self.cost = 0

    def add_card(self, card: Card) -> None:
        self.cards[card.name] = 1

    def remove_card(self, card_name: str) -> bool:
        pass

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        total = {"total_cards": len(self.cards)}
        self.cards = dict(total, **self.cards)
        self.cards["avg_cost"] = self.cost / len(self.cards)
        return f"Deck stats: {self.cards}"
