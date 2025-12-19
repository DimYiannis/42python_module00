
inventories = dict()


"""
setting up dicts that work as inventories
"""


inventories["Alice"] = {
    "sword": {"type": "weapon", "rarity": "rare", "qty": 1, "value": 500},
    "portion": {"type": "consumable", "rarity": "common", "qty": 5, "value": 50},
    "shield": {"type": "armor", "rarity": "uncommon", "qty":1, "value": 200}
}

inventories["Bob"] = {
    "portion": {"type": "consumable", "rarity": "common", "qty": 0, "value": 50}
}

"""
func where we show Alice's inventory
- create a new dict using items method to retrieve 
  all the key-val pairs
- use get which is a dict method to retrieve vals
-  since inv is a dict i assign each element to item->sword 
   and info->{type: ...., damage:...}
-   used  dict-method items to get key-val pairs

"""

def show_inventory(player):
    print(f"==={player}'s Inventory ===")
    
    inv = inventories.get(player, dict())
    total_value = 0
    total_items = 0
    category_count = dict()
    cat_summary = {}

    for item, info in inv.items():
        qty = info.get("qty", 0)
        val = info.get("value", 0)
        typ = info.get("type", "unknown")
        rarity = info.get("rarity", "common")
        print(f"{item} ({typ}, {rarity}): {qty}x @ {val} gold each = {qty*val} gold")
        total_value += qty*val
        total_items += qty
        if typ in category_count:
            category_count[typ] += qty
        else:
            category_count[typ] = qty

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    print(f"Categories: ")
    for k,v in category_count.items():
        dict_to_add = {k: v}
        cat_summary.update(dict_to_add)
        print(f"{k}({v})", end=", ")

show_inventory("Alice")

print("\n\n=== Transaction: Alice gives Bob 2 potions ===")
alice_inv = inventories.get("Alice")
bob_inv = inventories.get("Bob")

alice_portion = alice_inv.get("portion", {})
bob_portion = bob_inv.get("portion", {})

portion_qty = alice_portion.get("qty", 0)

if portion_qty >= 2:
    alice_portion["qty"] -= 2
    bob_portion["qty"] += 2
    print("Transaction successful!\n")
else:
    print("Transaction failed!\n")


print("=== Updated Inventories ===")
print(f"Alice potions: {alice_portion.get('qty',0)}")
print(f"Bob potions: {bob_portion.get('qty',0)}\n")


print("=== Inventory Analytics ===")
most_valuable = ("",0)
most_items = ("",0)
rarest_items = []

for player, inv in inventories.items():
    total_value = 0
    total_qty = 0
    for item, info in inv.items():
        value = info.get("value",0)
        qty = info.get("qty",0)
        rarity = info.get("rarity", "common")

        total_value += qty * value
        total_qty += qty 
        if rarity ==  "rare":
            rarest_items += [item]
    if total_value > most_valuable[1]:
        most_valuable = (player,total_value)
    if total_qty > most_items[1]:
        most_items = (player,total_qty)

print(f"Most valuable player: {most_valuable[0]} ({most_valuable[1]} gold)")
print(f"Most items: {most_items[0]} ({most_items[1]} items)")
result = ""
for item in rarest_items:
    if result == "":
        result = item
    else:
        result += ", " + item
print(f"Rarest items: {result}")


