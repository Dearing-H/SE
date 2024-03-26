import random

word_categories = []

esoteric_category = {
'category_name': "esoteric", 'words' :[ 'Axiom', 'Enigma', 'Paradox', 'Epiphany']
}

Technological_category = {
'category_name': "technological", 'words' :[ 'Network', 'Interface', 'Protocol', 'Integration']
}
Basketball_category = {
'category_name': "basketball", 'words' :[ 'Lebron', 'Tea Gardens', 'Spalding', 'Bird']
}

Entrances_category = {
'category_name': "entrances", 'words' :[ 'Portal', 'Doorway', 'Key', 'Passport']
}

Colours_category = {
'category_name': "colours", 'words' :[ 'red', 'green', 'blue', 'yellow']
}       

Cars_category = {
'category_name': "Cars", 'words' :[ 'fast', 'slow', 'SUV', 'sedane']
}       


Weather_category = {
'category_name': "Weather", 'words' :[ 'rain', 'wind', 'sun', 'cloudy']
}       

Sport_category = {
'category_name': "Sport", 'words' :[ 'football', 'tennis', 'pro wrestling', 'golf']
}       

multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category,Cars_category, Weather_category, Sport_category]

# def chosen_categories():
#     game_categories = []
#     for index in range(0,4):
#         random_index = random.randint(0,len(multiple_categories)-1)
#         game_categories.append(multiple_categories[random_index])
#         multiple_categories.pop(random_index)
#     return game_categories

# game_categories = chosen_categories()

