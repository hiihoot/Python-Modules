import sys
import os
import site


def main():
    in_venv = sys.prefix != sys.base_prefix

    if in_venv:
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("  python -m venv matrix_env")
        if os.name == "posix":
            print("  source matrix_env/bin/activate")
        else:
            print("  matrix_env\\Scripts\\activate")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
