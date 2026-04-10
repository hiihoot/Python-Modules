artifacts = [{'name': 'Ice Wand', 'power': 104, 'type': 'weapon'},
             {'name': 'Storm Crown', 'power': 84, 'type': 'armor'},
             {'name': 'Light Prism', 'power': 70, 'type': 'focus'},
             {'name': 'Storm Crown', 'power': 97, 'type': 'focus'}
             ]

mages = [{'name': 'Morgan', 'power': 62, 'element': 'shadow'},
         {'name': 'Storm', 'power': 85, 'element': 'lightning'},
         {'name': 'Storm', 'power': 90, 'element': 'shadow'},
         {'name': 'Jordan', 'power': 71, 'element': 'wind'},
         {'name': 'Ash', 'power': 79, 'element': 'lightning'}
         ]

spells = ['darkness', 'flash', 'tornado', 'fireball']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    print("Testing artifact sorter...")
    arti = sorted(artifacts, key=lambda a: a["power"], reverse=True)
    print(f"{arti[0]['name']} ({arti[0]['power']} power) "
          f"comes before {arti[1]['name']} ({arti[1]['power']} power)"
          )
    return arti


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    print("Testing spell transformer...")
    pow = list(filter(lambda p: p["power"] >= min_power, mages))
    return pow


def spell_transformer(spells: list[str]) -> list[str]:
    print("Testing spell transformer...")
    spells_star = list(map(lambda p: "* " + p + " * ", spells))
    for spell in spells_star:
        print(spell, end="")
    return spells_star


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": (max(mages, key=lambda max: max["power"]))["power"],
            "min_power": (min(mages, key=lambda min: min["power"]))["power"],
            "avg_power": round(sum(map(lambda v: v["power"], mages)) /
                               len(mages), 10)
            }


if __name__ == "__main__":
    artifact_sorter(artifacts)
    print()
    spell_transformer(spells)
