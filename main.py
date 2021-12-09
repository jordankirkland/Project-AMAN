import make_graph

print("Initiating...")
graph = make_graph.Graph()
print("Welcome to Project-AMAN")
print("a. Shortest Chain of Connection with Dijkstra's")
print("b. Shortest Chain of Connection with Breadth-First Search")

graph.Dijkstra2("Mel Gibson".lower(), "Jim Sturgess".lower())

print("done")