import sys
import math


def distance_calculator(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def main():
    print("=== Game Coordinate System ===\n")
    argv = sys.argv
    argc = len(argv)
    valid = True

    position = (10, 20, 5)
    print(f"Position created: {position}")
    print(f"Distance between (0, 0, 0) and "
          f"{position}:{distance_calculator(0, 0, 0, 10, 20, 5): .2f}\n")
    if (argc > 1):
        try:
            n = argv[1].split(",")
            x, y, z = int(n[0]), int(n[1]), int(n[2])
            print(f'Parsing coordinates: "{argv[1]}"')
        except Exception as e:
            valid = False
            print(f'Parsing invalid coordinates: "{argv[1]}"')
            print(f"Error parsing coordinat: {e}")
            print(f'Error details - Type: ValueError, Args: ("{e}")')
        if (valid):
            position = (x, y, z)
            print(f"Parsed position: {position}")
            print(f"Distance between (0, 0, 0) and "
                  f"{position}:{distance_calculator(0, 0, 0, x, y, z): .1f}\n")
    if (argc > 2):
        try:
            n = argv[2].split(",")
            x, y, z = int(n[0]), int(n[1]), int(n[2])
            print(f'Parsing coordinates: "{argv[2]}"')
        except Exception as e:
            valid = False
            print(f'Parsing invalid coordinates: "{argv[2]}"')
            print(f"Error parsing coordinates: {e}")
            print(f'Error details - Type: ValueError, Args: ("{e}")')
        if (valid):
            position = (x, y, z)
            print(f"Parsed position: {position}")
            print(f"Distance between (0, 0, 0) and "
                  f"{position}:{distance_calculator(0, 0, 0, x, y, z): .1f}\n")

        print("\nUnpacking demonstration:")
        print(f"Player at x={x} y={y} z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
