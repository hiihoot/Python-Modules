from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


def main() -> None:
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card:", [name for name in dir(Card) if "__" not in name][1:])
    print(
        "- Combatable:",
        [name for name in dir(Combatable) if "__" not in name][1:],
    )
    print(
        "- Magical:", [name for name in dir(Magical) if "__" not in name][1:]
    )

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    card = EliteCard("Arcane Warrior", 5, "Legendary", 5, 5, 10)
    print("Combat phase:")

    print("Attack result:", card.attack("Enemy"))
    print("Defense result:", card.defend(2))

    print("\nMagic phase:")
    print("Spell cast:", card.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", card.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
