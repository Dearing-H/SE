# import random

# word_categories = []

# esoteric_category = {
# 'category_name': "esoteric", 'words' :[ 'Axiom', 'Enigma', 'Paradox', 'Epiphany']
# }

# Technological_category = {
# 'category_name': "technological", 'words' :[ 'Network', 'Interface', 'Protocol', 'Integration']
# }
# Basketball_category = {
# 'category_name': "basketball", 'words' :[ 'Lebron', 'Tea Gardens', 'Spalding', 'Bird']
# }

# Entrances_category = {
# 'category_name': "entrances", 'words' :[ 'Portal', 'Doorway', 'Key', 'Passport']
# }

# colours = {
# 'category_name': "colours", 'words' :[ 'red', 'green', 'blue', 'yellow']
# }       

# cars = {
# 'category_name': "Cars", 'words' :[ 'fast', 'slow', 'SUV', 'sedane']
# }       


# weather = {
# 'category_name': "Weather", 'words' :[ 'rain', 'wind', 'sun', 'cloudy']
# }       

# sport = {
# 'category_name': "Sport", 'words' :[ 'football', 'tennis', 'pro wrestling', 'golf']
# }       

# multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, colours, cars, weather, sport]

# game_categories = []

# for index in range(0,4): # creating a list, for each entry decide the length
    
#     random_index = random.randint(0,len(multiple_categories)-1)

#     game_categories.append(multiple_categories[random_index])

#     multiple_categories.pop(random_index)

# for categorys in game_categories:
#     print(categorys["words"])


import random

# Define the list of word categories
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

# Add the categories to the list
# multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category]

# # Generate the game categories
# game_categories = []
# for index in range(0,4):
#     random_index = random.randint(0,len(multiple_categories)-1)
#     game_categories.append(multiple_categories[random_index])
#     multiple_categories.pop(random_index)

# Print the words for each category
# for category in game_categories:
#     print( category['words'])