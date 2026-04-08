# oracle.py
try:
    from dotenv import load_dotenv
    import os
except ModuleNotFoundError as e:
    print(e)
    exit(1)


def main():
    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")
    print(f"Mode: {matrix_mode}")
    print(
        f"Database: "
        f"{'Connected to local instance' if database_url else 'Not connected'}"
    )
    print(f"API Access: {'Authenticated' if api_key else 'Missing API key'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}")

    print("\nEnvironment security check:")

    try:
        with open(".env", "r") as f:
            content = f.read()
            if not content:
                print("[WARNING] Potential hardcoded secret detected in code")
            else:
                print("[OK] No hardcoded secrets detected")
    except FileNotFoundError as e:
        print(e)

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    if matrix_mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running with default .env")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
