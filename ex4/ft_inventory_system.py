"""Inventory Master: an inventory stored in a dictionary."""
import sys


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    """Build the inventory from '<item>:<quantity>' arguments."""
    inventory: dict[str, int] = {}
    for argument in arguments:
        parts: list[str] = argument.split(":")
        if len(parts) != 2 or parts[0] == "":
            print(f"Error - invalid parameter '{argument}'")
            '''
            continue - same use as return but for continue in the same function
            '''
            continue
        name: str = parts[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity: int = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue
        if quantity < 0:
            print(f"Quantity error for '{name}': negative quantity")
            continue
        inventory.update({name: quantity})
    return inventory


def analyse(inventory: dict[str, int]) -> None:
    """
    Print the item list, totals, shares and extreme items.
    Keys() - return names of the list
    inventory.values() - return only quantities
    """
    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    if total > 0:
        for name in items:
            share: float = round(inventory[name] / total * 100, 1)
            print(f"Item {name} represents {share}%")

    most: str = items[0]
    least: str = items[0]
    for name in items:
        """ Use the name as position in the list"""
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")


def main() -> None:
    """Entry point: parse, display, analyse and update the inventory."""
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    if len(inventory) == 0:
        print("Inventory is empty - nothing to analyse.")
    else:
        analyse(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
