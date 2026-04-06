import importlib
import sys


def main():
    modules = ["pandas", "requests", "matplotlib"]
    text = {
        "pandas": "Data manipulation ready",
        "requests": "Network access read",
        "matplotlib": "Visualization ready"
    }

    print("LOADING STATUS: Loading programs...\n")

    for m in modules:
        try:
            module = importlib.import_module(m)
            print(f"[OK] {module.__name__} ({module.__version__}) - "
                  f"{text[m]}")
        except ModuleNotFoundError:
            print("Use 'install -r requirements.txt' or 'peotry install'")
            break
    
    print(module)


if __name__ == "__main__":
    main()
