"""
used finally block to always dipslay a message in the try/except
in this func we go through eac plant and water it unless the name is invalid
"""


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


"""
create a list of plants and use
the above func for very plant in that list
"""


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print("Cleanup always happens, even with errors!")


test_watering_system()
