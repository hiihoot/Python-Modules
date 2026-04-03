from CreatureCard import CreatureCard


result = {
    "card_played": "Fire Dragon",
    "mana_used": 5,
    "effect": "Creature summoned to battlefield",
}


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    mana = fire_dragon.mana
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(mana)}")
    print("Play result:", fire_dragon.play(result))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))
    mana = fire_dragon.mana
    print(f"\nTesting insufficient mana ({mana} available)")
    print(f"Playable: {fire_dragon.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
