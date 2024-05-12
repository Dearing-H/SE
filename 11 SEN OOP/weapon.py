class Weapon:

    # constructor method 
    def __init__(self, name, damage, range, flavour_text):
        # attributes
        self.name = name # public
        self._damage = damage # private
        self.range = range
        self.flavour_text = flavour_text
        self.attack_speed = 0

    # methods
    def attack(self):
        import random
        damage = random.randint(1,10) * self._damage
        print(f"Attacking with {self.name} for {damage}")
        return damage

    # getter methods
    def get_damage(self):
        print(f'Current damage is {self._damage}')

    # setter methods
    def set_damage(self):
        print(f'Current damage is {self._damage}')
        damage_update = float(input("Please enter the new Weapon damage"))
        self._damage = damage_update
        print(f'Updated damage is {self._damage}')

class RangedWeapon(Weapon):
    def __init__(self, name, damage, range, flavour_text, ammo_type):
        super().__init__(name, damage, range, flavour_text)
        self.ammo_type = ""
        self.current_ammo = 30
    
    def attack(self): #Polymorphism
        if self.current_ammo >= 0:
            self.current_ammo -= 1
            print(f"The {self.name} shoots for {self._damage}")
        else:
            print(f"No projectiles left! Please reload")
        

togan = Weapon("Toogaa", 100, 50, "A toogan, what can i say")
rifle = RangedWeapon("M4A1", 1, 500, "A US issued full automatic rifle", "5.56mm")
bow = RangedWeapon("Wooden Bow", 0.5, 300, "A wooden bow", "Wooden Arrows")

for i in range(0,35):
    rifle.attack()

class Explosives(Weapon):
    def __init__(self, name, damage, range, flavour_text, area_damage,  ):
        super().__init__(name, damage, range, flavour_text)
        self.area_damage = ""
    
    def attack(self): #Polymorphism
        if self.current_ammo >= 0:
            self.current_ammo -= 1
            print(f"The {self.name} explodes for {self._damage}")
        else:
            print(f"No Expolsives left! Please reload")


C4 = Explosives("C4", 150, 60, "A bomb that you can set of from a distance",55 )


class 


    



#Inheritance allows developers to create subclasses from parent classes,
#and reuuse attributes and methods without the need to recocde them