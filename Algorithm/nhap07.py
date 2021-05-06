# # graph using tuple
# class Graph:
#     def __init__(self,edges):
#         self.edges = edges
#         self.graph_dict = {}
#         #create dict
#         for start, end in self.edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end]
#     def get_paths(self, start, end, path=[]):
#         #nếu lộ trình tới dc đích, đong khung nó lại và cho lộ trình tiếp theo
#         path = path + [start]
#         if start == end:
#             return [path]

#         if start not in self.graph_dict:
#             return []

#         paths = []
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 #represent for path (vi return path)
#                 new_paths = self.get_paths(node, end, path)
#                 for p in new_paths:
#                     paths.append(p)
#         return paths
#     def get_shortest_path(self, start, end, path=[]):
#         path = path + [start]

#         if start == end:
#             return path

#         if start not in self.graph_dict:
#             return None

#         shortest_path = None
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 sp = self.get_shortest_path(node, end, path)
#                 if sp:
#                     if shortest_path is None or len(sp) < len(shortest_path):
#                         shortest_path = sp

# routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris", "Dubai"),
#         ("Paris", "New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto"),
#     ]
# route_graph = Graph(routes)
# start = 'Mumbai'
# end = 'Toronto'

# print(route_graph.get_paths(start,end))


class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def get_vertices(self):
        return list(self.gdict.keys())
    def edges(self):
        return self.findedges()
    def findedges(self):
        edge_name = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex,vertex} not in edge_name:
                    edge_name.append({vertex,next_vertex})
        return edge_name
    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            if vertex2 not in self.gdict[vertex1]:
                self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = vertex2
        if vertex2 in self.gdict:
            if vertex1 not in self.gdict[vertex2]:
                self.gdict[vertex2].append(vertex1)
        else:
            self.gdict[vertex2] = vertex1

graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }
g = Graph(graph_elements)
g.addEdge({'a','e'})
g.addEdge({'a','c'})
print(g.gdict)