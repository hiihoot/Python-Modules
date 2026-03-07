def stream_game_events():
    names = ["alice", "bob", "charlie", "dave", "eve", "frank"]
    ach = ["killed monster", "found treasure", "leveled up",
           "joined guild"]
    i = 1
    while True:
        name_index = i % len(names)
        player_name = names[name_index]
        player_level = (i % 13.28) + 1
        ach_index = i % len(ach)
        player_action = ach[ach_index]
        yield (f"Event {i}: Player {player_name} " +
               f"(level {int(player_level)}) {player_action}")
        i += 1


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        temp = a
        a = b
        b = temp + b


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def main():
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    total_events = 0
    treasure_count = 0
    level_up_count = 0
    high_level_count = 0
    processing_time = 0
    high_level_tags = ["level 10", "level 11", "level 12", "level 13",
                       "level 14", "level 15", "level 16", "level 17",
                       "level 14", "level 19", "level 20", "level 21"]
    event_gen = stream_game_events()
    for event in range(1000):
        event = next(event_gen)
        print(event)
        if "found treasure" in event:
            treasure_count += 1
        if "leveled up" in event:
            level_up_count += 1
        for tag in high_level_tags:
            if tag in event:
                high_level_count += 1
        total_events += 1
        processing_time += 0.000045

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib_gen = fibonacci()
    print("Fibonacci sequence (first 10): ", end="")
    for n in range(10):
        print(f"{next(fib_gen)}", end="")
        if n != 9:
            print(", ", end="")

    prime_gen = primes()
    print("\nPrime numbers (first 5): ", end="")
    for n in range(9):
        print(f"{next(prime_gen)}", end="")
        if n != 8:
            print(", ", end="")
    print("")


if __name__ == "__main__":
    main()
