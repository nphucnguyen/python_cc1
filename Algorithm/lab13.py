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
    def shortestPath_BFS(self,start,goal):
        visited = set()
        # graph in the BFS
        queue = []
        queue.append(start)
        visited.add(start)
        # if the desired node is reached
        if start == goal:
            print('Same Node')
            return -1
        count =0
        count = self._shortestPath(visited,queue,goal,count)
        if goal not in visited:
            return -1
        return count
    def _shortestPath(self,visited,queue,goal,count):
        if queue == []:
            return count
        temp_queue = queue.copy()
        for vertex in temp_queue:
            queue.pop(0)
            for adjvertex in self.graph[vertex]:
                if adjvertex == goal:
                    visited.add(adjvertex)
                    count +=1
                    return count
                if adjvertex not in visited:
                    visited.add(adjvertex)
                    queue.append(adjvertex)
        count +=1
        return self._shortestPath(visited,queue,goal,count)
            
            





        # while queue:
        #     start = queue.pop()
        #     for adjvertice in self.graph[start]:
        #         if adjvertice not in visited:
        #             visited.add(adjvertice)
        #             queue.append(adjvertice)
        



        
g = Graph()
g.addEdge(1,4)
g.addEdge(1,3)
g.addEdge(2,5)
print(g.shortestPath_BFS(3,5))

#lab13.2
# class Graph():
 
#     def __init__(self, V):
#         self.V = V
#         self.graph = [[0 for column in range(V)] for row in range(V)]
 
#     def isBipartite(self, src):
#         # array contain separate bipart: 1 and 0 if it's fill
#         colorArr = [-1] * self.V
 
#         # Assign first color to source
#         colorArr[src] = 1
 
#         queue = []
#         queue.append(src)
 
#         # Run while there are vertices in queue
#         while queue:
 
#             u = queue.pop()
 
#             # Return false if there is a self-loop
#             if self.graph[u][u] == 1:
#                 return False
 
#             for v in range(self.V):
 
#                 # v is not colored
#                 if self.graph[u][v] == 1 and colorArr[v] == -1:
 
#                     # Assign alternate color to this
#                     # adjacent v of u
#                     colorArr[v] = 1 - colorArr[u]
#                     queue.append(v)
 
#                 # An edge from u to v exists and destination
#                 # v is colored with same color as u
#                 elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
#                     return False
 
#         # If we reach here, then all adjacent
#         return True
 
# g = Graph(4)
# g.graph = [[0, 1, 0, 1],
#             [1, 0, 1, 0],
#             [0, 1, 0, 1],
#             [1, 0, 1, 0]
#             ]
             
# print (1 if g.isBipartite(0) else 0)
 
