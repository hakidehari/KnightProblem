import random

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.weight = {}
        

    def getDict(self):
        return self.__graph_dict

    def assign_random_weight(self):
        assigned = {}
        for key in self.__graph_dict:
            for value in self.__graph_dict[key]:
                if not assigned[(key, value)] and not assigned[(value, key)]:
                    weight = random.randint(1, 50)
                    self.weight[str(key)+","+str(value)] = weight
                    self.weight[str(value)+","+str(key)] = weight
                    assigned[(key, value)] = True
                    assigned[(value, key)] = True


    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, vertex, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        self.__graph_dict[vertex].append(edge)

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if [vertex, neighbour] not in edges:
                    edges.append([vertex, neighbour])
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res