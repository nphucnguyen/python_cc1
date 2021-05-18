from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    def __str__(self):
        return str(dict(self.graph))
    def addEdge(self,u,v = None):
        if v is None:
            self.graph[u]
            return
        self.graph[u].add(v)
        self.graph[v].add(u)
    def BFS(self,s):
        # mark all the vertices as not visited
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)

        while queue:
            s = queue.pop(0)
            for adjvertice in self.graph[s]:
                if adjvertice not in visited:
                    visited.add(adjvertice)
                    queue.append(adjvertice)
        return visited

        
g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,3)
g.addEdge(4)
print(g.BFS(1))
