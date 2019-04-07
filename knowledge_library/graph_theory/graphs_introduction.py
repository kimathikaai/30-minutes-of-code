'''
Introduction into Graph  Theory Using Python
	Graph:
		Consists of 'nodes'/'verticies' and 'edges'/'connections'
			Edges can be directed ('arc') or not
		Nodes may or may not be connected to one another

'''

# Dictionaries are a good way to represent graphs in python
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
# An edge can be seen as a 2-tuple with nodes as elements, i.e.('a','b')

def generate_edges(graph):
    ''' Function to generate the list of all edges '''
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

'''
Example Output:
[('a', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('b', 'c'), 
('b', 'e'), ('e', 'c'), ('e', 'b'), ('d', 'c')]
'''

def find_isolated_nodes(graph):
    ''' Returns a list of isolated nodes '''
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)

    return isolated

'''
Example Ouput:
["f"]