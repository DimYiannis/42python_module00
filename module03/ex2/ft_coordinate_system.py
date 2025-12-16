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
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
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
    
    print(f"Position created: {coord}\n")
    print(f"Parsed position: ({x2}, {y2}, {z2})\n")
    res = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between (0, 0, 0) and ({coord}): {res}")
    
    new_coord = create_pos(sys.argv[1][0], sys.argv[1][1], sys.argv[1][2])
    x2 = new_coord[0]
    y2 = new_coord[1]
    z2 = new_coord[2]

    print(f"Parsing coordinates: {sys.argv}")
    print(f"Parsed position: ({x2}, {y2}, {z2})\n")
    print(f"Distance between (0, 0, 0) and ({sys.argv}): {res}")

    last_coord = create_pos("abc" ,"def" ,"ghi" )

    print("Unpacking demonstration:\n")
    print(f"Player at x={x2}, y={y2}, z={z2}\n")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")

