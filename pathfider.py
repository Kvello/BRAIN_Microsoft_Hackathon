from math import sqrt
import sys
import matplotlib.pyplot as plt

# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, edges, nodes):
        self.nodes = nodes
 
        # A list of lists to represent an adjacency list
        self.adjList = dict()
        for node in nodes:
            self.adjList[node] = []
        for (src, dest, weight) in edges:
            # allocate node in adjacency list from src to dest
            if dest.value != 0:
                self.adjList[src].append((dest, weight/dest.value))
 

class Node():
    def __init__(self, coord, val) -> None:
        self.coord = coord
        self.value = val

# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in graph.adjList.keys():
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src.coord} —> {dest.coord}, {weight}) ', end='')
        print()

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = graph.nodes
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.adjList[current_min_node]
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + (neighbor[1])
            if tentative_value < shortest_path[neighbor[0]]:
                shortest_path[neighbor[0]] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor[0]] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path
def dist(start_node, end_node):
    return sqrt((start_node.coord[0]-end_node.coord[0])**2+(start_node.coord[1]-end_node.coord[1])**2)#R2 norm

def get_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node.coord)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node.coord)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    path = reversed(path)
    return path

if __name__ == '__main__':
 
    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
    start_node = Node((0,0), 0)
    nodes = [Node((123, 22), 20), Node((43, 22), 55), Node((29, 68), 35), Node((103,77), 40), Node((26, 112),79),Node((76,45), 53)]
    end_node = (max(map(lambda node:(dist(start_node,node), node), nodes), key=lambda tuple: tuple[0]))[1]


    #edges = [(, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
    #       (4, 5, 1), (5, 4, 3)]
    edges = []
    nodes.append(start_node)
    for node1 in nodes:
        for node2 in nodes:
            if not node1 == node2:
                edges.append((node1, node2, dist(node1, node2)))

    img = plt.imread("sea.jpeg")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 165, 0, 140])
   
    #ax.set_ylim(0,10)
    x_values = []
    y_values = []
    for node in nodes:
        x_values.append(node.coord[0])
        y_values.append(node.coord[1])
        ax.annotate(str(node.value),xy=(node.coord[0],node.coord[1]+1))
    ax.plot(x_values, y_values, 'o', linewidth=5)

    #ax.set_ylim(0,10)
    

    # No. of vertices (labelled from 0 to 5)
    #n = 6
    # construct a graph from a given list of edges
    graph = Graph(edges, nodes)
 
    # print adjacency list representation of the graph
    #printGraph(graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph, start_node)
    path = get_result(previous_nodes, shortest_path, start_node, end_node)
    x_values = []
    y_values = []

    for (x,y) in path:
        x_values.append(x)
        y_values.append(y)
    ax.plot(x_values,y_values)
    plt.show()
    
