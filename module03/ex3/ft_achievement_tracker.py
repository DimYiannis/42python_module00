
inventories = dict()


"""
setting up dicts that work as inventories
"""


inventories["Alice"] = {
    "sword": {"type": "weapon", "rarity": "rare", "qty": 1, "value": 500},
    "potion": {"type": "consumable", "rarity": "common", "qty": 5, "value": 50}
    "shield": {"type": "armor", "rarity": "uncommon", "qty":1, "value": 200}
}

inventories["Bob"] = {
    "portion": {"type": "consumable", "rarity": "common", "qty": 0, "value": 50}
}

"""
func where we show Alice's inventory
"""

def show_inventory(player):
    print(f"==={player}'s Inventory ===")
    inv = inventories.get(player, dict())
    total_value = 0
    total_items = 0
    category_count = dict()
    for item, info in inv.items():
        qty = info.get("qty", 0)
        val = info.get("value", 0)
        typ = infor.get("type", "unknown")
        rarity = info.get("rarity", "common")
        print(f"{item} ({typ}, {rarity}): {qty}x {val} gold each = {qty*val} gold")
        total_values += qty*val
        total_items += qty
        category_count[typ] = category_count.get(typ, 0)+qty

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    for k,v in category_count.items())
        cat_summary = ", ".join(f"{k}({v})" 
    print(f"Categories: {cat_summary}\n")

show_inventory("Alice")

print("=== Transaction: Alice gives Bob 2 potions ===")
alice_inv = inventories.get("Alice")
bob_inv = inventories.get("Bon")
if alice_inv.get("portion", dict()).get("qty", 0) >= 2:
    alice_inv["portion"]["qty"] -= 2
    if "portion" not in bob_inv:
        bob_inv["potion"] = {"type":"consumable","rarity":"common","qty":0,"value":50}
    bob_inv["potion"]["qty"] += 2
    print("Transaction successful!\n")
else:
    print("Transaction failed!\n")


"""
Show updated inventories
"""
print("=== Updated Inventories ===")
print(f"Alice potions: {alice_inv.get('potion',dict()).get('qty',0)}")
print(f"Bob potions: {bob_inv.get('potion',dict()).get('qty',0)}\n")


"""
Inventory Analytics
"""


print("=== Inventory Analytics ===")
most_valuable = ("",0)
most_items = ("",0)
rarest_items = []

for player, inv in inventories.items():
    total_value = 0
    total_qty = 0
    for item, info in inv.items():
        total_value += info.get("qty",0)*info.get("value",0)
        total_qty += info.get("qty",0)
        if info.get("rarity","common") == "rare":
            rarest_items.append(item)
    if total_value > most_valuable[1]:
        most_valuable = (player,total_value)
    if total_qty > most_items[1]:
        most_items = (player,total_qty)

print(f"Most valuable player: {most_valuable[0]} ({most_valuable[1]} gold)")
print(f"Most items: {most_items[0]} ({most_items[1]} items)")
print(f"Rarest items: {', '.join(rarest_items)}")


