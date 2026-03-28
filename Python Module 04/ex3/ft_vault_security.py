def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    first_file = "classified_data.txt"
    second_file = "security_protocols.txt"
    try:
        print("Initiating secure vault access...")
        with open(first_file, "r+") as file:
            print(file.read())
            with open(second_file, "r") as file1:
                content = file1.read()
                print("\nSECURE PRESERVATION:")
                print(content)
            print("Vault automatically sealed upon completion")
            file.write(f"\n{content}")
    except Exception as e:
        print(e)
    else:
        print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
