import random

diffucluty_Level = {
    1: {'color': 'yellow', '\u001b[33m': 1},
    2: {'color': 'green', ' \u001b[32m': 2},
    3: {'color': 'blue', '\u001b[34m': 3},
    4: {'color': 'purple', '\u001b[35m': 4}
}


word_categories = []

esoteric_category = {
'category_name': "esoteric", 'Difficulty_Levels':2, 'words' :[ 'Axiom', 'Enigma', 'Paradox', 'Epiphany']
}

Technological_category = {
'category_name': "technological", 'Difficulty_levels':3, 'words' :[ 'Network', 'Interface', 'Protocol', 'Integration']
}
Basketball_category = {
'category_name': "basketball", 'Difficulty_levels':3, 'words' :[ 'Lebron', 'Tea Gardens', 'Spalding', 'Bird']
}

Entrances_category = {
'category_name': "entrances", 'Difficulty_levels':4, 'words' :[ 'Portal', 'Doorway', 'Key', 'Passport']
}

Colours_category = {
'category_name': "colours", 'Difficulty_levels':1, 'words' :[ 'Red', 'Green', 'Blue', 'Yellow']
}       

Cars_category = {
'category_name': "Cars", 'Difficulty_levels':2, 'words' :[ 'Fast', 'Slow', 'SUV', 'Sedane']
}       

Weather_category = {
'category_name': "Weather", 'Difficulty_levels':1, 'words' :[ 'Rain', 'Wind', 'Sun', 'Cloudy']
}       

Sport_category = {
'category_name': "Sport", 'Difficulty_levels':1, 'words' :[ 'Football', 'Tennis', 'Pro-wrestling', 'Golf']
}       

Shakespeare_category = { 
'category_name': "Shakespeare", 'Difficulty_levels':2, 'words' :[ 'Sonnets', 'Romeo', 'Tragedy', 'Hamlet'  ]
}

Ancient_Military_category = { 
'category_name': "Ancient Military", 'Difficulty_levels':3, 'words' :[ 'Legion', 'Phalanx', 'Hoplites', 'Triarii'  ]
}

Mythological_Creatures_category = {
'category_name': "Mythological Creatures ", 'Difficulty_levels':3, 'words' :[ 'Griffin', 'Centaur', 'Phoenix', 'Minotaur']
}     

Avant_Garde_Art_Movements = {
'category_name': "Avant-Garde Art Movements ", 'Difficulty_levels':3, 'words' :[ 'Dadaism', 'Cubism', 'Surrealism', 'Fluxus']
}

Quantum_Mechanics_Concepts = {
'category_name': "Quantum Mechanics Concepts ", 'Difficulty_levels':4, 'words' :[ 'Superposition', 'Quantum Tunneling', 'Entanglement', 'Resistance']
}

Literary_Devices = {
'category_name': "Literary Devices ", 'Difficulty_levels':4, 'words' :[ 'Metonymy', 'Synecdoche', 'Chiasmus', 'Anaphora']
}

Fast_and_Furious_Locations = {
'category_name': "Fast and Furious Locations ", 'Difficulty_levels':3, 'words' :[ 'Los Angeles', 'Rio de Janeiro', 'Tokyo', 'Abu Dhabi']
}

multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category,Cars_category, Weather_category, Sport_category, Shakespeare_category, 
                       Ancient_Military_category, Mythological_Creatures_category, Avant_Garde_Art_Movements, Quantum_Mechanics_Concepts, Literary_Devices, Fast_and_Furious_Locations,     ]


def get_color_and_index(difficulty_level):
    return difficulty_level.get(difficulty_level, {'color': 'white', 'index': 0})  # Default to white if difficulty level not found

# Assign color codes and indices to categories based on difficulty levels
# for category in word_categories:
#     color_info = get_color_and_index(category['difficulty_level'])
#     category['color'] = color_info['color']
#     category['color_index'] = color_info['index']






#colour of diffuclut
#change the colour of the cateogry