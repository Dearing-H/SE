import random

# Define the categories
esoteric_category = {"words": ["abjure", "cabal", "defenestration", "elixir", "hierophant", "labyrinthine", "necromancy", "obfuscate"]}
Technological_category = {"words": ["algorithm", "bandwidth", "cache", "debug", "encryption", "firewall", "gigabyte", "hackathon"]}
Basketball_category = {"words": ["alley-oop", "backboard", "court", "dribble", "foul", "half-court", "jump shot", "layup"]}
Entrances_category = {"words": ["arch", "doorway", "gate", "portal", "stoop", "threshold", "vestibule", "welcome mat"]}
sport = {"words": ["baseball", "basketball", "football", "golf", "hockey", "lacrosse", "soccer", "tennis"]}
weather = {"words": ["blizzard", "drizzle", "fog", "gale", "hail", "ice", "lightning", "monsoon"]}
cars = {"words": ["convertible", "diesel", "electric", "ford", "gasoline", "hybrid", "jeep", "kia"]}
colours = {"words": ["black", "blue", "cyan", "green", "indigo", "magenta", "orange", "purple"]}

all_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, sport, weather, cars, colours]

# Define the grid
grid = [["Word", "Word", "Word", "Test"],
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"]]

def random_categories():
    random_categories = random.sample(all_categories, 4)
    for i in range(4):
        grid[i][3] = random_categories[i]
        for j in range(len(random_categories[i]["words"])):
            grid[i][i] = random_categories[i]["words"][j]
    return grid

random_categories()
print(grid)