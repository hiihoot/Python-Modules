def test_error_types():
    try:
        print("Testing ValueError...")
        a = "abc"
        b = int(a)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        c = 0
        b = 0
        b = c / b
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'\n")
    try:
        print("Testing KeyError...")
        plant = {"Flower": "Rose"}
        plant["missing_plat"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    try:
        print("Testing multiple errors together...")
        a = "abc"
        b = int(a)

        c = 0
        b = 0
        b = c / b

        open("missing.txt", "r")
        plant = {"Flower": "Rose"}
        plant["missing_plat"]
    except (ValueError, KeyError, ValueError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
