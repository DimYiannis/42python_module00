"""
creating sets of achievements
"""

alice_set = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob_set = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie_set = {
    "level_10",
    "treasure_hunter",
    "boss_slayer",
    "speed_demon",
    "perfectionist",
}

print("=== Achievement Tracker System ===")

print(f"Player alice achievements: {alice_set}")
print(f"Player bob achievements: {bob_set}")
print(f"Player charlie achievements: {charlie_set}\n")


"""
use union to get all the unique achievements
"""


print("=== Achievement Analytics ===")
all_unique = alice_set.union(bob_set, charlie_set)
print(f"All unique achievements: {all_unique}")
print(f"Total unique achievements: {len(all_unique)}\n")


"""
- with intersection method we get the common achievements
- make a set of rare achievements and see
how many players have them
- add to the rare_found_in_players set rare achievements
  found from each player using |=
"""

common_to_all = alice_set.intersection(bob_set, charlie_set)
print(f"Common to all players: {common_to_all}")

rare = {"collector", "perfectionist"}
rare_found_in_players = set()
player_count = 0
if rare.intersection(alice_set):
    player_count += 1
    rare_found_in_players |= rare.intersection(alice_set)
if rare.intersection(bob_set):
    player_count += 1
    rare_found_in_players |= rare.intersection(bob_set)
if rare.intersection(charlie_set):
    player_count += 1
    rare_found_in_players |= rare.intersection(charlie_set)

if player_count > 1:
    message = f"{player_count} players"
elif player_count == 1:
    message = f"{player_count} player"
else:
    message = "no players"

print(f"Rare achievements ({message}): {rare_found_in_players}\n")

print(f"Alice vs Bob common: {alice_set.intersection(bob_set)}")
print(f"Alice unique: {alice_set.difference(bob_set)}")
print(f"Bob unique: {bob_set.difference(alice_set)}")
