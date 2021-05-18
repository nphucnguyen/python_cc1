class AdjNode:
    # Node have vertex
    def __init__(self, value):
        self.vertex = value
        self.next = None


# class by linkedlist
class Graph:
    def __init__(self, num):
        # The number of vertex
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        # begin with index s(vertex s), put in the head
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        # begin with index d(vertex d), put in the head
        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
    print(graph)