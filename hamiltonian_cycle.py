def hamiltonian_cycle(graph):
   
    start_vertex = 0 
    path = [start_vertex]
    visited = {start_vertex}

    if backtrack_hamiltonian_cycle(graph, start_vertex, path, visited):
        return path 
    else:
        return None  

def backtrack_hamiltonian_cycle(graph, current_vertex, path, visited):
    num_vertices = len(graph)

    if len(path) == num_vertices:
        
        if graph[path[-1]][path[0]] == 1:
            return True  # Hamiltonian cycle is found
        else:
            return False  # The last vertex does not have an edge to the starting vertex

    for next_vertex in range(num_vertices):
        if graph[current_vertex][next_vertex] == 1 and next_vertex not in visited:
            path.append(next_vertex)
            visited.add(next_vertex)

            if backtrack_hamiltonian_cycle(graph, next_vertex, path, visited):
                return True

          
            path.pop()
            visited.remove(next_vertex)

    return False  


graph_matrix = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0]
    ]


h_cycle=hamiltonian_cycle(graph_matrix)

if h_cycle:
    print(f'hamiltonian cycle {h_cycle}')
else:
    print('could not find any cycle!!!')
