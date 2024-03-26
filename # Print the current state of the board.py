import random

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, node):
        self.connections.append(node)
        node.connections.append(self)

    def __repr__(self):
        return f"{self.name} connected to {[n.name for n in self.connections]}"


# Create nodes
nodes = [Node(f"Node {i}") for i in range(10)]

# Connect nodes randomly
for node in nodes:
    possible_connections = [n for n in nodes if n != node]
    num_connections = random.randint(1, len(possible_connections))
    for _ in range(num_connections):
        random_node = random.choice(possible_connections)
        node.connect(random_node)
        possible_connections.remove(random_node)

# Print connections
for node in nodes:
    print(node)