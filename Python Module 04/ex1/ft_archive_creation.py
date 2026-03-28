def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    enterys = ["New quantum algorithm discovered",
               "Efficiency increased by 347%",
               "Archived by Data Archivist trainee"]
    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open(file_name, "w")
        print("Storage unit created successfully...\n")
    except Exception as e:
        print(e)
    else:
        print("Inscribing preservation data...")
        i = 1
        for entery in enterys:
            file.write(f"[ENTERY 00{i}]{entery}\n")
            print(f"[ENTRY 00{i}]", entery)
            i += 1
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation")


if __name__ == "__main__":
    main()
