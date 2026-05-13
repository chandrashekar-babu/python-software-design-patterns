from copy import deepcopy
from typing import Any

class Prototype:
    def clone(self) -> 'Prototype':
        """Create a deep copy of this object."""
        return deepcopy(self)

class GameCharacter(Prototype):
    def __init__(self, name: str, health: int, inventory: list):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.equipped_items: list[str] = []
    
    def __deepcopy__(self, memo):
        # Custom cloning: share equipped items but copy inventory
        cls = self.__class__
        new_character = cls.__new__(cls)
        memo[id(self)] = new_character
        
        new_character.name = self.name
        new_character.health = self.health
        new_character.inventory = deepcopy(self.inventory, memo)
        new_character.equipped_items = self.equipped_items  # Shared reference
        
        return new_character

# Usage
hero_template = GameCharacter("Hero", 100, ["sword", "potion"])
hero1 = hero_template.clone()
hero2 = hero_template.clone()
print(f"Hero1 Inventory: {hero1.inventory}, Equipped: {hero1.equipped_items}")
print(f"Hero2 Inventory: {hero2.inventory}, Equipped: {hero2.equipped_items}")