class Person:
    def __init__(self,height, shoe_size,name,eye_colour,number_of_kidney,favourite_car,best_artist):
        #ATTRIBUTES
        self.height = height
        self.shoe_size = shoe_size
        self.name = name
        self.eye_colour = eye_colour
        self.number_of_kidney = number_of_kidney
        self.favourite_car = favourite_car
        self.best_artist = best_artist

        #METHODS
    def scream(Self):
        print("ARGHHHHHHH!!")
    
Boss = Person(6.6,14,"Boss","Blue",2,"Mustang Gt","Travis Scott")
print(Boss)