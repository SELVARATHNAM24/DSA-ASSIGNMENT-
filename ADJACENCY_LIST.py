class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adjacency_list = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Add an edge between two vertices
    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist in the graph
        self.add_vertex(vertex1)  
        self.add_vertex(vertex2)  
        self.adjacency_list[vertex1].append(vertex2)
        # Add the reverse edge for an undirected graph
        self.adjacency_list[vertex2].append(vertex1)

    # Display the adjacency list
    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

# for an undirected graph 
graph = Graph()  

# Add edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

# Display the adjacency list
graph.display()
