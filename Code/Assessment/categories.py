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

Artistic_category = {
'category_name': "artistic", 'Difficulty_levels':3, 'words' :[ 'Painting', 'Sculpture', 'Drawing', 'Photography']
}

Musical_category = {
'category_name': "musical", 'Difficulty_levels':3, 'words' :[ 'Piano', 'Guitar', 'Violin', 'Drums']
}

Culinary_category = {
'category_name': "culinary", 'Difficulty_levels':3, 'words' :[ 'Recipe', 'Ingredient', 'Cuisine', 'Cooking']
}


Historical_category = {
'category_name': "historical", 'Difficulty_levels':3, 'words' :[ 'Ancient', 'Medieval', 'Renaissance', 'Modern']
}

Geographical_category = {
'category_name': "geographical", 'Difficulty_levels':3, 'words' :[ 'Mountain', 'River', 'Desert', 'Island']
}

Literary_Types_category = {
'category_name': "literary", 'Difficulty_levels':3, 'words' :[ 'Novel', 'Poetry', 'Drama', 'Fiction']
}

Scientific_category = {
'category_name': "scientific", 'Difficulty_levels':3, 'words' :[ 'Experiment', 'Hypothesis', 'Theory', 'Observation']
}

Cultural_category = {
'category_name': "cultural", 'Difficulty_levels':3, 'words' :[ 'Tradition', 'Custom', 'Festival', 'Ceremony']
}

Fashion_category = {
'category_name': "fashion", 'Difficulty_levels':3, 'words' :[ 'Style', 'Design', 'Trend', 'Accessory']
}

Nature_category = {
'category_name': "nature", 'Difficulty_levels':3, 'words' :[ 'Forest', 'Ocean', 'Sky', 'Sunset']
}

Business_category = {
'category_name': "business", 'Difficulty_levels':3, 'words' :[ 'Entrepreneur', 'Marketing', 'Finance', 'Strategy']
}

Medical_category = {
'category_name': "medical", 'Difficulty_levels':3, 'words' :[ 'Doctor', 'Patient', 'Hospital', 'Treatment']
}

Educational_category = {
'category_name': "educational", 'Difficulty_levels':3, 'words' :[ 'Learning', 'Teaching', 'School', 'Knowledge']
}

Political_category = {
'category_name': "political", 'Difficulty_levels':3, 'words' :[ 'Government', 'Democracy', 'Election', 'Policy']

}
Environmental_category = {
'category_name': "environmental", 'Difficulty_levels':3, 'words' :[ 'Climate', 'Conservation', 'Ecosystem', 'Pollution']
}












multiple_categories = [esoteric_category, Technological_category, Basketball_category, Entrances_category, Colours_category, Cars_category, Weather_category, Sport_category, Shakespeare_category, 
                       Ancient_Military_category, Mythological_Creatures_category, Avant_Garde_Art_Movements, Quantum_Mechanics_Concepts, Literary_Devices, Fast_and_Furious_Locations,
                       Artistic_category, Musical_category, Culinary_category, Historical_category, Geographical_category, Literary_Types_category, Scientific_category, Cultural_category, Fashion_category, 
                       Nature_category, Business_category, Medical_category, Educational_category, Political_category, Environmental_category
                       ]

def get_color_and_index(difficulty_level):
    return difficulty_level.get(difficulty_level, {'color': 'white', 'index': 0})  # Default to white if difficulty level not found

# Assign color codes and indices to categories based on difficulty levels
# for category in word_categories:
#     color_info = get_color_and_index(category['difficulty_level'])
#     category['color'] = color_info['color']
#     category['color_index'] = color_info['index']






#colour of diffuclut
#change the colour of the cateogry