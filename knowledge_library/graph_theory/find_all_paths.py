from graphs_class import Graph

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths("a", "b")
print(path)

print('All paths from vertex "a" to vertex "f":')
path = graph.find_all_paths("a", "f")
print(path)

print('All paths from vertex "c" to vertex "c":')
path = graph.find_all_paths("c", "c")
print(path)

'''
EXPECTED OUTPUT:

Vertices of graph:
['a', 'b', 'c', 'd', 'e', 'f']
Edges of graph:
[{'a', 'd'}, {'f', 'a'}, {'c', 'b'}, {'c'}, {'c', 'd'}, {'e', 'c'}, {'f', 'd'}]
All paths from vertex "a" to vertex "b":
[['a', 'd', 'c', 'b'], ['a', 'f', 'd', 'c', 'b']]
All paths from vertex "a" to vertex "f":
[['a', 'f']]
All paths from vertex "c" to vertex "c":
[['c']]
'''