

def main():
    print("=== Achievement Tracker System ===\n")
    ach = [
            'first_kill', 'level_10',
            'treasure_hunter', 'speed_demon',
            'boss_slayer', 'collector',
            'treasure_hunter', 'speed_demon',
            'perfectionist'
          ]
    alice = {ach[0], ach[1], ach[2], ach[3]}
    bob = {ach[0], ach[1], ach[4], ach[5]}
    charlie = {ach[1], ach[2], ach[4], ach[7], ach[8]}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")
    common = alice.intersection(bob, charlie)
    print(f"Common to all players: {common}")
    alice_only = alice.difference(bob, charlie)
    bob_only = bob.difference(alice, charlie)
    charlie_only = charlie.difference(alice, bob)
    rare_ach = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {rare_ach}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
