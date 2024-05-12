from weapon import Weapon
from player import Player
from enemy import Enemy
# instantiate a weapon 

game_weapons = []

starter_weapon = Weapon(
    "Rock",
    1.0,
    0.5,
    "It's a rock, not much to it than that"
)
game_weapons.append(starter_weapon)

booma = Weapon(
    "Booma",
    2.0,
    10.0,
    "A spherical ball of solid plasma, used by the Gungan armies against the Trade Federation's armies during the battle of Theed."
)
game_weapons.append(booma)

nicks_fored = Weapon(
    "Nick's Forehead",
    999.0,
    0.5,
    "It's a giant blunt object, came from something hollow"
)


game_weapons.append(nicks_fored)

laser_glasses = Weapon(
    "Laser Glasses",
    10.0,
    100.0,
    "It's very fancy"
)
game_weapons.append(laser_glasses)


cheese_wheel = Weapon(
    "Wheel of Cheese",
    50.0,
    0.7,
    "A big, heavy wheel of fresh swiss cheese"
)
game_weapons.append(cheese_wheel)

darksaber = Weapon(
    "Dark Saber",
    25.0,
    2.5,
    "The ancient Blade belonging to Mand'alor Tarre Vizsla, the first Mandalorian to be taken in by the Jedi Order. Now a symbol of Authority amongst the Mandalorians, it has been passed down through their Emperors for 1000 years."
)

game_weapons.append(darksaber)


jittleyang_slingshot = Weapon(
    "the jittleyang slingshot",
    2000,
    1000,
    "The Jittleyang sling shot is a compact launcher designed for propelling tiny Jittleyang creatures with precision. Load, aim, and release for strategic chaos and exhilarating fun."
)
game_weapons.append(jittleyang_slingshot)

johnson = Weapon(
    "Flaming Johnson",
    69.0,
    10.0,
    "Long reach, Hard hitting"
)

game_weapons.append(johnson)

chakram = Weapon(
    "Chakram",
    25.0,
    15.0,
    "A powerful melee and throwing blade that can do massive damage"
)
game_weapons.append(chakram)

import random
random_item_from_fishers_basement = Weapon(
    "random item from fishers basement",
    random.randint(1, 1000 ),
    random.randint(1, 1000 ),
    "this is a random item you pull of of the bag that you found in josh fishers basement!, could do a lot of damage or very little")

game_weapons.append(random_item_from_fishers_basement)


starter_weapon = Weapon(
    "Minion",
    999999,
    0.00000001,
    "very angry midget creature")

game_weapons.append(starter_weapon)

knowledge = Weapon(    
"knowledge",     
0.00001,     
10000000000000000000000000000,     
"Most people lack knowledge, but our young hero does not.")

game_weapons.append(knowledge)

sniper = Weapon(
    "Heavy Sniper",
    300,
    50,
    "Bro don't peak he has a sniper"
) 

game_weapons.append(sniper)

toogan = Weapon(
    "Toogan",
    10000,
    5,
    """Toogan, one of the jittleyangs is a very dark, black bird.
    In the case that joogan edges to his full potential,
    he releases a massive explostion of goon across the village."""
)

game_weapons.append(toogan)

brax = Player("Brax the 🇮🇹")
brax.equip_weapon(jittleyang_slingshot)



enemies = []
# instantiate 99 enemies
for i in range (99):
    x = Enemy()
    enemies.append(x)

print(enemies)

brax.attack(enemies[0])
