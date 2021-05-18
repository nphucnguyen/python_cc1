# xuat phat tu depth first search
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    def addEdge(self, u , v = None):
        # self.graph[u].add(v)
        # if v == None:
        #     return
        # self.graph[v].add(u)
        if v == None:
            self.graph[u]
            return
        self.graph[u].add(v)
        self.graph[v].add(u)
    def __str__(self):
        return str(dict(self.graph))
    def DFS(self,v):
        #create a set to store visited vertices
        visited = set()
        #call the recusive helper function
        self._DFS(v,visited)
        return visited
    def _DFS(self,v,visited):
        # mark the current node as visited
        visited.add(v)
        for adjVertex in self.graph[v]:
            if adjVertex not in visited:
                self._DFS(adjVertex,visited)
    def connectionBetween2Vertex(self,u,v):
        visited = self.DFS(u)
        if v in visited:
            return 1
        else:
            return 0
    
            
    
    





# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# print(dfs(graph, '0'))
graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(4)
print(graph)
print(graph.connectionBetween2Vertex(4,2))
