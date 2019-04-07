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

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + ' '
        res += '\nedges: '
        for edges in self.__generate_edges():
            res += str(edge) + ' '
        return res

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

    def find_path(self, start_vertex, end_vertex, path=None):
        ''' Find a path from start_vertex to end_vertex in graph '''
        if path == None:
            path = []

        graph = self.__graph_dict
        path += [start_vertex]

        if start_vertex == end_vertex:
            return  path
        if start_vertex not in graph:
            return None
            
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extend_path = self.find_path(vertex, end_vertex, path)
                if extend_path:
                    return extend_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        ''' Find all paths from start_vertex to end_vertex in graph '''
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
        
    '''
    DEGREE:
        The degree of a vertex in a graph is the number of edges connecting it,
        with loops counted twice ('a'-'a')

    REGULAR GRAPH:
        If all the degrees in a graph are the same, the graph is a regular graph

    THE DEGREE SUM FORMULA (HANDSHAKING LEMMA):
        The sum of degrees of all vertices = number of edges * 2
        We can conclude that the number of vertices with odd degree has to be even

    '''
    def vertex_degree(self,vertex):
        ''' Find the degree of a vertex '''
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_isolated_vertices(self):
        ''' Returns a list of isolated vertices '''
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            if len(graph[vertex]) == 0:
                isolated += [vertex]
        return isolated

    def delta(self):
        ''' Find the minimum degree of the vertices '''
        graph = self.__graph_dict
        vertices_size = [self.vertex_degree(vertex) for vertex in graph]
        return min(vertices_size)

    def Delta(self):
        ''' Find the maximum degree of the vertices '''
        graph = self.__graph_dict
        vertices_size = [self.vertex_degree(vertex) for vertex in graph]
        return max(vertices_size)

    '''
    DEGREE SEQUENCE:
        The sequence of its vertex degrees in non-increasing order (5,2,1,1,0)

    '''
    def degree_sequence(self):
        ''' Calculates the degree sequence of a graph '''
        seq = []
        graph = self.__graph_dict
        for vertex in graph:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    '''
    Erd"os Gallai Theorem:
        Tells you when a sequence of integers occurs as the sequence of degrees of a simple
        graph. 'Simple' means no loops or repeated edges
    '''
    @staticmethod
    def erdoes_gallai(input_sequence):
        ''' Checks if the conditions for the Erdoes-Gallai theorem '''
        # Check if the sum of elements of the sequence is odd
        if sum(input_sequence) % 2:
            return False

        for k in range(1,len(input_sequence) + 1):
            left = sum(input_sequence[:k])
            right = k * (k-1) + sum([min(x,k) for x in input_sequence[k:]])
            if left > right:
                return False
        return True



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
