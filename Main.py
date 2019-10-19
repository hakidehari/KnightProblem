from Graph import Graph

def shortest_path(knight_graph, paths):
    #knight_graph.assign_random_weight()
    min_cost = 9999999
    total = 0
    lowest = ""
    for path in paths:
        for i in range(0, len(path)-1):
            total += knight_graph.weight[str(path[i])+","+str(path[i+1])]
        if total < min_cost:
            min_cost = total
            print(min_cost)
            lowest = path
        total = 0
    return lowest


#add all the vertices to the graph
def add_vertices_to_graph(knight_graph, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            knight_graph.add_vertex((i, j))
    return knight_graph


#add all possible edges to the graph (288 in total for a 10x10 board)
def add_edges_to_graph(knight_graph, rows, cols):
    for coordinate in knight_graph.getDict():
        row_index = coordinate[0]
        col_index = coordinate[1]
        if row_index-2 in range(0, rows) and col_index+1 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index-2, col_index+1))
        if row_index-1 in range(0, rows) and col_index+2 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index-1, col_index+2))
        if row_index+1 in range(0, rows) and col_index+2 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index+1, col_index+2))
        if row_index+2 in range(0, rows) and col_index+1 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index+2, col_index+1))
        if row_index+2 in range(0, rows) and col_index-1 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index+2, col_index-1))
        if row_index+1 in range(0, rows) and col_index-2 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index+1, col_index-2))
        if row_index-1 in range(0, rows) and col_index-2 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index-1, col_index-2))
        if row_index-2 in range(0, rows) and col_index-1 in range(0, cols):
            knight_graph.add_edge(coordinate, (row_index-2, col_index-1))
    return knight_graph


# Function to print a BFS of graph 
def BFS(knight_graph, src, dest, count=0): 
    # Mark all the vertices as not visited 
    visited = {}
    for key in knight_graph.getDict():
        visited[key] = False
    # Create a queue for BFS 
    queue = [] 
    # Mark the source node as  
    # visited and enqueue it 
    queue.append(src) 
    visited[src] = True
    while queue: 
        # Dequeue a vertex from  
        # queue and print it 
        src = queue.pop(0) 
        print (str(src)+" ") 
        count+=1
        if src == dest:
            return count-1
        # Get all adjacent vertices of the 
        # dequeued vertex s. If a adjacent 
        # has not been visited, then mark it 
        # visited and enqueue it 
        for i in knight_graph.getDict()[src]: 
            if visited[i] == False: 
                queue.append(i) 
                visited[i] = True


def BFS_modified(knight_graph, src, dest):
    queue = [(src, [src])]
    while queue:
        (vertex, path) = queue.pop(0)
        for u in set(knight_graph.getDict()[vertex]) - set(path):
            if u == dest:
                yield path + [u]
            else:
                queue.append((u, path + [u]))


def DFS_modified(knight_graph, src, dest, path=None):
    if path is None:
        path = [src]
    if src == dest:
        yield path
        print(path)
    for u in set(knight_graph.getDict()[src]) - set(path):
        yield from DFS_modified(knight_graph, u, dest, path + [u])


def DFSUtil(src, dest, visited, knight_graph, count=0): 
    # Mark the current node as visited  
    # and print it 
    visited[src] = True
    print(str(src)+" ") 
    count+=1
    if src == dest:
        return count-1
    # Recur for all the vertices  
    # adjacent to this vertex 
    for i in knight_graph.getDict()[src]: 
        if visited[i] == False: 
            return DFSUtil(i, dest, visited, knight_graph, count) 


def DFS(src, dest, knight_graph): 
    # Mark all the vertices as not visited 
    visited = {}
    for key in knight_graph.getDict():
        visited[key] = False
    # Call the recursive helper function  
    # to print DFS traversal 
    count = DFSUtil(src, dest, visited, knight_graph)
    return count



def dijsktra(knight_graph, src, dest):
    #initialize
    d = {}
    pi = {}
    for vertex in knight_graph.getDict():
        d[vertex] = 9999999
        pi[vertex] = None
    d[src] = 0

    Q = list(knight_graph.getDict().keys())
    while len(Q) > 0:
        u = Q.pop(0)
        if u == dest:
            S = []
            u = dest
            if pi[u] is not None or u == src:
                while u is not None:
                    S.append(u)
                    u = pi[u]
        for v in knight_graph.getDict()[u]:
            alt = d[u]+1
            if alt < d[v]:
                d[v] = alt
                pi[v] = u
    
    return S




#generate the graph
def generate_knight_graph(board):
    knight_graph = Graph()
    rows = len(board)
    cols = len(board[0])
    knight_graph = add_vertices_to_graph(knight_graph, rows, cols)
    knight_graph = add_edges_to_graph(knight_graph, rows, cols)
    knight_graph.assign_default_weight()
    print("DONE GENRATING GRAPH")
    return knight_graph


def findGold(n, knightrow, knightcol, goldrow, goldcol):
    #generates chess boaerd based on n
    board = [[0 for i in range(n)] for j in range(n)]
    knight_graph = generate_knight_graph(board)
    #print(BFS(graph, (knightrow,knightcol), (goldrow,goldcol)))
    #print(DFS((2,2), (2,3), graph))
    #print(dijsktra(graph, (2,2), (2,3)))

    BFS_paths = list(BFS_modified(knight_graph, (knightrow, knightcol), (goldrow, goldcol)))
    print("done generating BFS paths")
    BFS_shortest_path = shortest_path(knight_graph, BFS_paths)
    print("BFS shortest path is: "+str(BFS_shortest_path))

    DFS_paths = list(DFS_modified(knight_graph, (knightrow, knightcol), (goldrow, goldcol)))
    print("done generating DFS paths")
    DFS_shortest_path = shortest_path(knight_graph, DFS_paths)
    print(DFS_paths)
    print("DFS shortest path is: "+ str(DFS_shortest_path))


if __name__ == '__main__':
    findGold(5, 2, 2, 3, 2)



