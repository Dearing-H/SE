#Q1
games = ["Fornite","Minecraft", "Among US"]
games.insert(0, "Rocket League")

print(games)

#Q2
road_trip = ("New York", "Los Angeles",5, ["John", "Peter", "Sam"])
print(road_trip[1])

#Q3
your_cards = {"Bulbasaur", "Squirtle", "Mewtwo","Gible"}
harrison_cards = {"Bulbasaur", "Charizard", "Pikachu", "Litten"}
print(your_cards.difference(harrison_cards))

#Q4
scores = [100, 200, 300, 400]
average = sum(scores)/len(scores)

total = 0
for score in scores:
    total += score
print(total/len(scores))