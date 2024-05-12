import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self._weapon = 0
        self.inventory = [] # limit 2

    def equip_weapon(self,weapon):
        print("Equipping a weapon...")
        time.sleep(2)
        self._weapon = weapon
        print(f"Equipped a {self._weapon.name}")

    def pickup_weapon(self,weapon):
        print("Picking up an item")

        if len(self.inventory) >= 2:
            print("Unable to pickup item")
            print("You are over-encumbered")
        else:
            self.inventory.append(weapon)
        
    def display_inventory(self):
        print("Printing inventory...")
        print(self.display_inventory)
        for weapon in self.inventory:
            print(weapon.name)
            print(weapon.flavour_text)

    def attack(self,enemy):
        print(f"You attack a {enemy.name}")
        print(f"They have {enemy.hp} HP remaining")
        damage = self._weapon.attack()
        enemy.hp -= damage
        print(f"They have {enemy.hp} HP remaining after attacking")
        # need to reduce the enemy HP