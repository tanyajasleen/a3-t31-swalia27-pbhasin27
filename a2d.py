# This class demonstrate the Graph
class Graph:
    def __init__(self, number_of_verts):
        """
        This method creates the Graph object
        and create an adjacency matrix of give number of vertices
        with default weight value 0
        :param number_of_verts: total vertices of the graph
        """
        self.num_vertes = number_of_verts
        self.adjmat = [[0 for i in range(self.num_vertes)] for j in range(self.num_vertes)]

    def add_vertex(self):
        """
        This method add new vertex in the graph
        :return: Nothing to return
        """
        tmparr = self.adjmat  # copy existing adjacency matrix
        tvert = self.num_vertes
        self.num_vertes += 1  # increase vertices by one
        # initialize new adjacency matrix with updated vertices
        self.adjmat = [[0 for i in range(self.num_vertes)] for j in range(self.num_vertes)]
        # copy old data to newly adjacency matrix
        for i in range(0, tvert):
            for j in range(0, tvert):
                self.adjmat[i][j] = tmparr[i][j]

    def add_edge(self, from_idx, to_idx, weight=1):
        """
        This method add new edge in the adjacency matrix/Graph
        :param from_idx: starting vertex
        :param to_idx: ending vertex
        :param weight: edge weight
        :return: True if edge is added False otherwise
        """
        if not (0 <= from_idx < self.num_vertes):
            return False
        if not (0 <= to_idx < self.num_vertes):
            return False
        if self.adjmat[from_idx][to_idx] != 0:
            return False
        self.adjmat[from_idx][to_idx] = weight
        return True

    def num_edge(self):
        """
        This method count the total edges in the Graph
        :return: Total edges in the Graph
        """
        count = 0
        for i in range(0, self.num_vertes):
            for j in range(0, self.num_vertes):
                if self.adjmat[i][j] != 0:
                    count += 1
        return count

    def num_verts(self):
        """
        :return: Total vertices in the Graph
        """
        return self.num_vertes

    def has_edge(self, from_idx, to_idx):
        """
        This method check whether edge exists between give two vertices
        :param from_idx: starting vertex
        :param to_idx: endging vertex
        :return: True if edge exists between give vertices False otherwise
        """
        if not (0 <= from_idx < self.num_vertes):
            return False
        if not (0 <= to_idx < self.num_vertes):
            return False
        if self.adjmat[from_idx][to_idx] == 0:
            return False
        return True

    def edge_weight(self, from_idx, to_idx):
        """
        This metod find the weight of the edge of give two vertices
        :param from_idx: starting vertex
        :param to_idx: ending vertex
        :return: weight of the edge if it exists None otherwise
        """
        if not (0 <= from_idx < self.num_vertes):
            return None
        if not (0 <= to_idx < self.num_vertes):
            return None
        if self.adjmat[from_idx][to_idx] == 0:
            return None
        return self.adjmat[from_idx][to_idx]

    def get_connected(self, v):
        """
        This method find the vertices which are directly connected with given vertex 'v'
        :param v: source vertex
        :return: list of destination vertex along with weight if found, empty list otherwise
        """
        res = []
        if not (0 <= v < self.num_vertes):
            return res
        for j in range(0, self.num_vertes):
            if self.adjmat[v][j] != 0:
                res.append((j, self.adjmat[v][j]))
        return res

    # Following code is not the part of the  assignment
    # It is used to check the working of above code

    def disp(self):
        for i in range(0, self.num_vertes):
            for j in range(0, self.num_vertes):
                print(self.adjmat[i][j], sep=" ", end=" ")
            print()


