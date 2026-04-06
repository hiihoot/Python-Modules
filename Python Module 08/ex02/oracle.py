try:
    from dotenv import load_dotenv
    import os
except ModuleNotFoundError as e:
    print(e)


def main():
    load_dotenv()
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Mode:", matrix_mode)
    if database_url:
        print("Database:", "Connected to local instance")
    else:
        print("Database:", "Not connected to local instance")
    if api_key:
        print("API Access:", "Authenticated")
    else:
        print("API Access:", api_key)
    print("Log Level:", log_level)
    if zion_endpoint:
        print("Zion Network:", "Online")
    else:
        print("Zion Network:", "Offline")

    print("\nEnvironment security check:")
    try:
        file = ".env"
        with open(file, "r")



if __name__ == "__main__":
    main()
