from a2d import Graph
from a3b import minimum_spanning_tree
import random


def generate_maze(number_of_rows, number_of_columns):
    """
    This method generate the maze from the given row and columns.
    It uses the graph and MST to create the wall of the Maze
    :param number_of_rows: no of rows in the Maze
    :param number_of_columns:  no of columns in the Maze
    :return: walls of the Maze
    """
    list_of_walls = []
    c1 = 0
    c2 = -1
    # Nested Loops to create the list of wall in column order
    for i in range(number_of_rows):
        c2 += 1
        for j in range(number_of_columns - 1):
            c1 = c2
            c2 += 1
            list_of_walls.append((c1, c2))
    # Nested Loops to create the list of wall in row order
    for j in range(number_of_columns):
        c1 = j
        for i in range(number_of_rows - 1):
            list_of_walls.append((c1, c1 + number_of_columns))

            c1 = c1 + number_of_columns
    #print("Inital Wall List")
    #print(list_of_walls)
    graph = Graph(number_of_rows * number_of_columns)
    # create Adjacency Matrix in graph to store the wall and its random weights
    for edge in list_of_walls:
        wt = random.randint(1, 50)
        graph.add_edge(edge[0], edge[1], wt)
        graph.add_edge(edge[1], edge[0], wt)
    print("Adjacency Matrix")
    #graph.disp()
    # find the minimum spannig tree from teh give graph
    mst = minimum_spanning_tree(graph)
    #print("MST")
    #print(mst)
    # Delete the walls which are in minimum spanning tree
    for edge in mst:
        if edge in list_of_walls:
            list_of_walls.remove(edge)
        else:
            edge1 = (edge[1], edge[0])
            list_of_walls.remove(edge1)
    #print("Final Wall List")
    #print(list_of_walls)
    return list_of_walls # the maze with remaining list of walls



