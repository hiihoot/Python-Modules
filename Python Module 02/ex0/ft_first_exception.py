def check_temperature(temp_str: str):
    '''
    Demonstrating basic error handling
    used Exception because its has all common errors
    '''
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Testing temperature: {temp_str}")
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if temp_int < 0:
            print(f"Testing temperature: {temp_int}")
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
        elif temp_int > 40:
            print(f"Testing temperature: {temp_int}")
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Testing temperature: {temp_int}")
            print("Temperature 25°C is perfect for plants!\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")
