class Graph:
    def __init__(self):
        # Initialize an empty dictionary for the adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an edge between two vertices
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # Comment this line for a directed graph

    def remove_edge(self, vertex1, vertex2):
        # Remove an edge between two vertices
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)  # Comment this line for a directed graph

    def remove_vertex(self, vertex):
        # Remove a vertex and its edges
        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent].remove(vertex)
            del self.adjacency_list[vertex]

    def display(self):
        # Display the adjacency list
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")

# Example usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

print("Graph:")
graph.display()

graph.remove_edge("A", "C")
print("\nAfter removing edge A-C:")
graph.display()

graph.remove_vertex("B")
print("\nAfter removing vertex B:")
graph.display()