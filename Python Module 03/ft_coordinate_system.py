import sys
import math


def distance_calculator(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def main():
    print("=== Game Coordinate System ===\n")
    argv = sys.argv
    valid = True

    position = (10, 20, 5)
    print(f"Position created: {position}")
    print(f"Distance between (0, 0, 0) and " 
          f"{position}:{distance_calculator(0, 0, 0, 10, 20, 5): .2f}\n")
    try:
        n = argv[1].split(",")
        x, y, z = int(n[0]), int(n[1]), int(n[2])
    except ValueError as e:
        valid = False
        print(f'Parsing invalid coordinates: {e.args}')
        print(f"Error parsing coordinat: {e}")
    if (valid):
        position = (x, y, z)
        print(f"Position created: {position}")
        print(f"Distance between (0, 0, 0) and " 
              f"{position}:{distance_calculator(0, 0, 0, x, y, z): .1f}\n")
        print("Unpacking demonstration:")
        print(f"Player at x={x} y={y} z={z}")
        print("Coordinates: X={x}, Y={y} z={z}")

if __name__ == "__main__":
    main()
