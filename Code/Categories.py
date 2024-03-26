import random

# word_categories = []

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

colours = {
'category_name': "cryptic", 'words' :[ 'red', 'green', 'blue', 'yellow']
}       

cars = {
'category_name': "cryptic", 'words' :[ 'fast', 'slow', 'SUV', 'sedane']
}       


weather = {
'category_name': "cryptic", 'words' :[ 'rain', 'wind', 'sun', 'cloudy']
}       

sport = {
'category_name': "cryptic", 'words' :[ 'football', 'tennis', 'pro wrestling', 'golf']
}       

multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, colours, cars, weather, sport]

game_categories = []

for index in range(0,4): # creating a list, for each entry decide the length
    
    random_index = random.randint(0,len(multiple_categories)-1)

    game_categories.appened(multiple_categories[random_index])

    multiple_categories.remove(multiple_categories[random_index])

for categorys in game_categories:
    print(categorys["Words"])
