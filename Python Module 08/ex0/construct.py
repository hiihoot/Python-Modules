import sys
import os
import site


def main():
    original_path = sys.base_prefix
    current_path = sys.prefix

    if original_path != current_path:
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(current_path))
        print("Environment Path:", current_path)

        print(("\nSUCCESS: You're in an isolated environment!"
              "Safe to install packages without affecting"
               "the global system."))
        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!\n"
              "The machines can see everything you install\n")

        print("To enter the construct, run: python -m venv matrix_env")
        print("-> python -m venv matrix_env")
        if os.name == "posix":
            print("-> source matrix_env/bin/activate")
        else:
            print("-> matrix_env Scripts activate")

        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
