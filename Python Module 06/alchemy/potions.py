from alchemy.elements import (create_air, create_earth,
                              create_fire, create_water)

FIRE = create_fire()
AIR = create_air()
EARTH = create_earth()
WATER = create_water()


def healing_potion():
    return f"Healing potion brewed with {FIRE} and {WATER}"


def strength_potion():
    return f"Strength potion brewed with {EARTH} and {FIRE}"


def invisibility_potion():
    return f"Invisibility potion brewed with {AIR} and {WATER}"


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: "
            f"{WATER, AIR, EARTH, FIRE}")
