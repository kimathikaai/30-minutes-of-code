from graphs_class import Graph 

g = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

complete_graph = { 
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
}

isolated_graph = { 
    "a" : [],
    "b" : [],
    "c" : []
}


graph = Graph(g)
print(graph.density())

graph = Graph(complete_graph)
print(graph.density())

graph = Graph(isolated_graph)
print(graph.density())