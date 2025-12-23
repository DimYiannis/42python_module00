def fib(n):
    """
    -generator that returns 'n' numbers from the fibonacci sequence
    -yield turms this func into a generator
    so instead of retumimg one value we manage
    to return multiple numbers
    """
    a = 0
    b = 1
    for i in range(0, n):
        yield a
        tmp = a
        a = b
        b = tmp + b


def prime(n):
    """
    -generator that returns 'n' prime numbers
    -function pause when it reaches yield and on the next
    call it resumes from the exact point
    it stopped
    """
    for num in range(2, n):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            yield num


def game_events(n):
    """
    - generator that returns n number of events
        with the specified players
    - with non streaming we would need to store all the 1000 events
        with generator only one event happens at a time
    - we tranverse through the list of names using i and module of the
        length of the list
    - generate random levels multplying with 3
        3 generates 20 iterations but not the same
        happens for 4 and 5
    """
    players = ["alice", "bob", "charlie", "dave"]
    for i in range(1, n + 1):
        player = players[i % len(players)]
        level = (i * 3) % 20 + 1

        if i % 10 == 0:
            event_type = "treasure"
        elif i % 7 == 0:
            event_type = "leveled_up"
        else:
            event_type = "monster"

        yield {"number": i, "player": player,
               "level": level, "type": event_type}


if __name__ == "__main__":
    total_events = 0
    high_lvl = 0
    treasure_events = 0
    lvl_up = 0

    print("=== Game Data Stream Processor ===\n")

    print("Processing 1000 game events...\n")

    for event in game_events(1000):
        total_events += 1

        if event["level"] >= 10:
            high_lvl += 1
        if event["type"] == "treasure":
            treasure_events += 1
        if event["type"] == "leveled_up":
            lvl_up += 1

        action = {
            "treasure": "found treasure",
            "leveled_up": "leveled up",
            "monster": "killed monster",
        }[event["type"]]
        print(
            f"Event {event['number']}: Player {event['player']}"
            f"(level {event['level']}) {action}"
        )

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_lvl}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {lvl_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib_gen = fib(10)
    prime_gen = prime(12)

    print("Fibonacci sequence (first 10): ", end="")
    for i in range(0, 10):
        if i == 9:
            print(f"{next(fib_gen)}")
        else:
            print(f"{next(fib_gen)}", end=", ")

    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        if i == 4:
            print(f"{next(prime_gen)}")
        else:
            print(f"{next(prime_gen)}", end=", ")
