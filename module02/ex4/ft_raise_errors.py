"""
checking if name is okk then
throw errors if water level is not right
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!\n")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f"is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f"is too high (max 12)\n")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        message = check_plant_health("tomato", 5, 6)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("carrot", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


test_plant_checks()
