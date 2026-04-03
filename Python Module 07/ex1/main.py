from ex1.Deck import Deck
from ex0 import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()
    creatues = CreatureCard("Fire Dragon", 6, "Legendary", 7, 5)
    artifacts = ArtifactCard("artifacts", 5, "yes", "very", "true")
    spells = SpellCard("spells", 5, "yes", "very")
    deck.cost = creatues.cost
    deck.cost += artifacts.cost
    deck.cost += spells.cost

    deck.add_card(creatues)
    deck.add_card(spells)
    deck.add_card(artifacts)
    print(deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    light_bolt = SpellCard("Lightning Bol", 2, "moderate", "light")
    print(f"Drew: {light_bolt.name}")
    game_data = {'card_played': 'Lightning Bolt',
                 'mana_used': 3, 'effect': 'Deal 3 damage to target'}
    print("Play result:", light_bolt.play(game_data))


if __name__ == "__main__":
    main()
