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
g.dijstra(0)
             
 
