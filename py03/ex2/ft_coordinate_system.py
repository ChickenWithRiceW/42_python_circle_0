import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        in_str = input("Enter new coordinates as floats in format 'x,y,z': ")
        input_list = in_str.strip().split(',')
        tmp = []
        try:
            if len(input_list) != 3:
                raise Exception("Invalid syntax")
            for i in input_list:
                tmp.append(float(i))
        except Exception:
            print("Invalid syntax")
        else:
            return (tmp[0], tmp[1], tmp[2])


def get_distance(pos0: tuple[float, float, float],
                 pos1: tuple[float, float, float] = (0.0, 0.0, 0.0)) -> float:
    x1, y1, z1 = pos0
    x2, y2, z2 = pos1
    distance = (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return round(distance, 4)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos0 = get_player_pos()
    print(f"Got a first tuple: {pos0}")
    print(f"It includes: X={pos0[0]} Y={pos0[1]} Z={pos0[2]}")
    print(f"Distance to center: {get_distance(pos0)}")

    print("Get a second set of coordinates")
    pos1 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{get_distance(pos0, pos1)}")


if __name__ == "__main__":
    main()
