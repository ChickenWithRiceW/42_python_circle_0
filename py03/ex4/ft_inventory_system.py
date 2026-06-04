import sys

WHITE = "\033[97m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"


def main() -> int:
    inventory_dict: dict[str, int] = {}
    argc = len(sys.argv)
    if argc < 2:
        print("Usage: ./ft_inventory_system.py <item_name>:<quantity> ...")
        return 1

    for item in sys.argv[1:]:
        if ':' not in item:
            print(f"Error - invalid parameter '{item}'")
            continue

        item_name, item_quantity_str = item.lower().split(':', 1)
        try:
            item_quantity = int(item_quantity_str)
        except Exception as e:
            print(f"Quantity error for '{item_name}': {e}")
        else:
            if item_name not in inventory_dict.keys():
                inventory_dict[item_name] = item_quantity
            else:
                print(f"{YELLOW}Redundant item '{item_name}' - discarding"
                      f"{RESET}")

    total_items = len(inventory_dict.keys())
    total_quantity = sum(list(inventory_dict.values()))

    # ! So that programm doesn't crash
    if total_items < 1:
        return 1

    print(f"Got inventory: {inventory_dict}")
    print(f"Item list: {list(inventory_dict.keys())}")
    print(f"Total quantity of the {total_items} items: "
          f"{total_quantity}")

    for item in inventory_dict.keys():
        percentage = round(((inventory_dict[item] / total_quantity) * 100), 2)
        print(f"Item {item} represents {percentage}%")

    item_max = ""
    for item in inventory_dict.keys():
        for to_compare in inventory_dict.keys():
            if inventory_dict[to_compare] > inventory_dict[item]:
                break
        else:
            item_max = item
            break

    item_min = ""
    for item in inventory_dict.keys():
        for to_compare in inventory_dict.keys():
            if inventory_dict[item] > inventory_dict[to_compare]:
                break
        else:
            item_min = item
            break
    print(f"Item most abundant: {item_max} with quantity "
          f"{inventory_dict[item_max]}")
    print(f"Item least abundant: {item_min} with quantity "
          f"{inventory_dict[item_min]}")

    inventory_dict.update({"Secret_weapon": 1})
    print(inventory_dict)
    return 0


if __name__ == "__main__":
    main()
