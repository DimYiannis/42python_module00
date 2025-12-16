import sys
import math


def create_pos(x, y, z):
    coord = ()
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        coord = (x, y, z)
        return coord
    except ValueError as e:
        print(f"Parsing invalid coordinates: {x},{y},{z}")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")
    coord = create_pos(10, 20, 5)
    x2 = coord[0]
    y2 = coord[1]
    z2 = coord[2]

    x1 = 0
    y1 = 0
    z1 = 0

    print(f"Position created: {coord}")
    res = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between (0, 0, 0) and ({coord}): {res}\n")
    res = float(res)

    new_coord_str = sys.argv[1]
    x2, y2, z2 = new_coord_str.split(",")
    new_coord = create_pos(x2, y2, z2)
    res = math.sqrt((int(x2) - x1)**2 + (int(y2) - y1)**2 + (int(z2) - z1)**2)
    res = float(res)

    print(f"Parsing coordinates: {sys.argv[1]}")
    print(f"Parsed position: ({x2}, {y2}, {z2})")
    print(f"Distance between (0, 0, 0) and ({new_coord_str}): {res}\n")

    last_coord = create_pos("abc", "def", "ghi")

    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
