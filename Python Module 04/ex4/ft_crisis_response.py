def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file_name = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        with open(file_name, "r") as file:
            file.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except Exception:
        print("Unexpected error happened")

    file_name = "classified_vault.txt"
    print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        with open(file_name, "r") as file:
            file.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained")
    except Exception:
        print("Unexpected error happened")

    file_name = "standard_archive.txt"
    print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
    try:
        with open(file_name) as file:
            print(f"SUCCESS: Archive recovered - ''{file.read()}''")
    except Exception:
        print("Unexpected error happened")
    else:
        print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
