import alchemy


def main():
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): ", end="")
    print(alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", end="")
    print(alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", end="")
    print(alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", end="")
    print(alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): ", end="")
    print(alchemy.create_fire())
    print("alchemy.create_water(): ", end="")
    print(alchemy.create_water())
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not expose")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not expose")
    print("\nPackage metadata: ")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
