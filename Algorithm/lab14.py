#lab14.1
#thuat toan dijstra
class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] for row in range(V)]
 
    def dijstra(self, src):
        #Set T about vertice that isn't calculate yet
        set_T = {_ for _ in range(self.V)}
        min_distance = [float('inf')] * self.V
        pre_meet = [-1] * self.V
        min_distance[src] = 0
        set_T.discard(src)
        pre_meet[src] = src
        cur_vertex = src
        self._dijstra(cur_vertex,pre_meet,min_distance,set_T)
        print(min_distance)
        print(pre_meet)
        return min_distance, pre_meet
    def _dijstra(self,cur_vertex,pre_meet,min_distance,set_T):
        if set_T == set():
            return(pre_meet,min_distance)

        #find the future vertex to cosider
        min_future_vertex_distance = float('inf')


        for vertex in set_T:
            #print(type(vertex))
            #if have edge between 2 vertex
            if self.graph[cur_vertex][vertex] !=0:
                temp_distance = min_distance[cur_vertex] + self.graph[cur_vertex][vertex]
                if temp_distance < min_distance[vertex]:
                    min_distance[vertex] = temp_distance
                    pre_meet[vertex] = cur_vertex

                # find the future vertex
                if min_distance[vertex] < min_future_vertex_distance:
                    min_future_vertex_distance = min_distance[vertex]
                    furture_vertex = vertex
        set_T.discard(furture_vertex)
        self._dijstra(furture_vertex,pre_meet,min_distance,set_T)






g = Graph(4)
g.graph = [[0, 2, 5, 0],
            [2, 0, 1, 2],
            [5, 1, 0, 3],
            [0, 2, 3, 0]
            ]
min_distance, pre_meet  = g.dijstra(0)


#lab14.2 kt xem có chứa chu kì có trọng số âm hay không
#bellman-ford algorithm
class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print('1')
                return
        print('0')
        return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, -2)
g.add_edge(2, 3, -3)
g.add_edge(3, 1, 4)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 2)

g.bellman_ford(0)

 
