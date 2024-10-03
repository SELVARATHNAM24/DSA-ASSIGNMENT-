class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:  
            self.graph[v] = []
    
    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)
    
    def topological_sort(self):
        visited = {key: False for key in self.graph}
        stack = []
        
        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)
        
        return stack[::-1]

 
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort of the given graph:")
print(g.topological_sort())
