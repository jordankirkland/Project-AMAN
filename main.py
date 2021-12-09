import make_graph

print("Initiating graph...")
graph = make_graph.Graph()
print("Graph initialized!")
print("Welcome to Project-AMAN.")

while True:
    print("1. Find the degree of separation between two actors with Breadth-First Search.")
    print("2. Find the degree of separation between two actors and the path that connects them with Dijkstra's.")
    print("3. Find the number of unique actors an actor has been in a movie with and display them.")
    print("4. Find the number of movies an actor has been in and list them.")
    print("5. Exit the program")
    selection = input("Please select an operation: ")

    if selection == "1":
        actor1 = input("Please input the first actor's first and last name: ")
        actor2 = input("Please input the second actor's first and last name: ")
        graph.BFS2(actor1.lower(), actor2.lower())
    elif selection == "2":
        actor1 = input("Please input the first actor's first and last name: ")
        actor2 = input("Please input the second actor's first and last name: ")
        graph.Dijkstra(actor1.lower(), actor2.lower())
    elif selection == "3":
        actor = input("Please input the actor's first and last name: ")
        
        # Edge case for actor not in the graph
        try:
            graph.lookUp[actor]
        except KeyError:
            print("Invalid actor name. Please try again.")
            continue
        
        actors = graph.lookUp[actor.lower()].actors
        print(graph.lookUp[actor.lower()].name + " has been in a movie with " + str(len(actors)) + " other unique actors.")
    elif selection == "4":
        actor = input("Please input the actor's first and last name: ")
        
        # Edge case for actor not in the graph
        try:
            graph.lookUp[actor]
        except KeyError:
            print("Invalid actor name. Please try again.")
            continue

        movies = graph.lookUp[actor.lower()].movies
        print(graph.lookUp[actor.lower()].name + " has been in " + str(len(movies)) + " movie(s). They are listed below:")
        print(movies)
    elif selection == "5":
        break
    else:
        print("Invalid input. Please try again.")

        # Printing an extra line to improve readability (NEEDS FIXING IDK)
        print("\n")