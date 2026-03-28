def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    try:
        file = open(file_name, "r")
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...\n")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
    except Exception as e:
        print(f"ERROR: {e}")
    else:
        print("RECOVERED DATA:")
        print(file.read())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
