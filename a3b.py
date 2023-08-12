from a2d import Graph
from a3a import MinHeap


# This class stores the edge of the weighted undirected graph
# It also overloads the comparison operators to work with the edge instance
class Edge:
    def __init__(self, startv, endv, wt):
        self.startv = startv
        self.endv = endv
        self.wt = wt

    def __lt__(self, other):
        if self.wt < other.wt:
            return True
        return False

    def __gt__(self, other):
        if self.wt > other.wt:
            return True
        return False

    def __ge__(self, other):
        if self.wt >= other.wt:
            return True
        return False


def minimum_spanning_tree(graph):
    """
    This method find the minimum cost path in the give graph using Prim's algorithms
    :param graph: Graph for which minimum spanning tree is built
    :return: Tuples of Minimum spanning tree edges
    """
    visited = [False for v in range(graph.num_verts())]  # array to keep track the visited vertex
    minheap = MinHeap()  # Min heap to store and find the edge with minimum weight
    mst = []
    edge = 0
    visited[0] = True
    while edge < graph.num_edge():  # Loop to get all the edges of the graph
        for startvertx in range(graph.num_verts()):  # Loop to get starting vertex of the edges
            if visited[startvertx]:  # if vertex is already in the minimum spanning tree
                for endvertx in range(graph.num_verts()):  # Get the edges
                    # find the edges of the fringe vertices and store in the min heap
                    if not visited[endvertx] and graph.edge_weight(startvertx, endvertx) is not None:
                        vedge = Edge(startvertx, endvertx, graph.edge_weight(startvertx, endvertx))
                        minheap.insert(vedge)

        if not minheap.is_empty():
            res = minheap.extract_min()  # get the edge with minimum weight
            minedge = (res.startv, res.endv)
            mst.append(minedge)  # ada it to the minimum spanning tree
            visited[res.endv] = True  # set the vertex as visited
            while not minheap.is_empty():  # Empty the minheap
                minheap.extract_min()
        edge += 1  # count the edges
    return mst


# Following code checks the working of minimum spanning tree and not the part of Part B solution

'''
# Graph 1
graph = Graph(7)
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 0, 2)
graph.add_edge(1, 4, 4)
graph.add_edge(1, 6, 5)
graph.add_edge(2, 0, 3)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 2, 1)
graph.add_edge(3, 4, 2)
graph.add_edge(4, 1, 4)
graph.add_edge(4, 3, 2)
graph.add_edge(4, 5, 4)
graph.add_edge(5, 4, 4)
graph.add_edge(5, 6, 1)
graph.add_edge(6, 1, 5)
graph.add_edge(6, 5, 1)
print(minimum_spanning_tree(graph))
'''
'''
# Graph 2
graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 0, 4)
graph.add_edge(1, 2, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(2, 1, 8)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 5, 4)
graph.add_edge(2, 8, 2)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(4, 3, 9)
graph.add_edge(4, 5, 10)
graph.add_edge(5, 2, 4)
graph.add_edge(5, 3, 14)
graph.add_edge(5, 4, 10)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 5, 2)
graph.add_edge(6, 7, 1)
graph.add_edge(6, 8, 6)
graph.add_edge(7, 0, 8)
graph.add_edge(7, 1, 11)
graph.add_edge(7, 6, 1)
graph.add_edge(7, 8, 7)
graph.add_edge(8, 2, 2)
graph.add_edge(8, 6, 6)
graph.add_edge(8, 7, 7)
print(minimum_spanning_tree(graph))
'''
'''
# Graph 3
graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 7)
graph.add_edge(1, 2, 11)
graph.add_edge(1, 3, 9)
graph.add_edge(1, 5, 20)
graph.add_edge(2, 5, 1)
graph.add_edge(3, 6, 6)
graph.add_edge(3, 4, 2)
graph.add_edge(4, 6, 10)
graph.add_edge(4, 8, 15)
graph.add_edge(4, 7, 5)
graph.add_edge(4, 5, 1)
graph.add_edge(5, 7, 3)
graph.add_edge(6, 8, 5)
graph.add_edge(7, 8, 12)
print(minimum_spanning_tree(graph))
'''
