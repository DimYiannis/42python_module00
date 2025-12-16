"""
we use try except bloke to check if the
value of temp is acceptible, throw value
error if input is not int
"""


def check_temperature(temp_str):
    print("=== Garden Temperature Checker ===")

    try:
        t = int(temp_str)
        print(f"Testing temperature: {t}")
        if t > 40:
            print(f"Error: {t}°C is too hot for plants (max 40°C)\n")
        elif t < 0:
            print(f"Error: {t}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {t}°C is perfect for plants\n")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number \n")


def test_temperature_input():

    check_temperature(25)
    check_temperature(100)
    check_temperature("abc")
    check_temperature(-10)
    print("All tests completed - program didn't crash!")


test_temperature_input()
