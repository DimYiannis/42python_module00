import sys
import math


class Players:
    def __init__(self):
        self.players = {}

    def create_player(self, name, x, y, z):
        try:
            self.players[name] = (x, y, z)
        except ValueError as {e}:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    def get_player_coord(self, name)
        return self.players[name]

print("=== Game Coordinate System ===")

if len
