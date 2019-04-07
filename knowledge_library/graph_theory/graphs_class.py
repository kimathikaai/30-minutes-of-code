''' A Python Class
A simple Python graph class, demonstrating the essential facts
and functionalities of graphs.
'''

class Graph:
    def __init__(self, graph_dict=None):
        ''' Initializes a graph object, If no dictionary or None
        is given, an empty dictionary will be use
        '''
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        # Double underscore for 'name mangling'

    def vertices(self):
        ''' Returns the vertices of a graph '''
        return list(self.__graph_dict.keys())

    def edges(self):
        ''' returns the edges of a graph '''
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        ''' Assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges
        '''
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        ''' A static method generating the edges of the graph
            Edges are represented as sets with on (a loop back to the vertex)
            or two vertices
        '''
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})

        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + ' '
        res += '\nedges: '
        for edges in self.__generate_edges():
            res += str(edge) + ' '

        return res


def main():
    initial_graph = { 
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
    }

    graph = Graph(initial_graph)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
  

if __name__ == "__main__":
    main()
