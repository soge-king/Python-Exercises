# This dictionary represents a weighted graph where each key is a node and 
#the associated values are tuples of connected nodes with their respective weights.
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# This function calculates the shortest path from a start node to a target node 
#(optional) in a given graph using a variation of Dijkstra's algorithm.
def shortest_path(graph, start, target=''):
    # Create a list of all nodes that have not been visited yet.
    unvisited = list(graph)
    # Initialize distances from the start node to all other nodes as infinity, except the start node which is set to zero.
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # Tracks the actual paths from the start node to each other node.
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    # Continue the algorithm until all nodes have been visited.
    while unvisited:
        # Select the unvisited node with the smallest distance to the start node.
        current = min(unvisited, key=distances.get)
        # Update the shortest distances to neighboring nodes and track the paths.
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                paths[node] = paths[current] + [node]
        # Mark the current node as visited by removing it from the unvisited list.
        unvisited.remove(current)
    
    # Determines which nodes to print the distances and 
    #paths for; defaults to all if no target specified.
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Return the calculated distances and paths.
    return distances, paths

# Call the function to calculate and print the shortest path and distances from 'A' to 'F'.
shortest_path(my_graph,'A' ,'F')
