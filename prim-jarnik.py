import heapq


class Vertex:

    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjacency_list = []

    def __str__(self):
        return self.data


class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    def __lt__(self, other):
        return self.weight < other.weight


class PrimsJarnik:

    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list
        self.spanning_tree = []
        self.edge_heap = []
        self.full_cost = 0

    def calculate_spanning_tree(self, vertex):
        self.unvisited_list.remove(vertex)

        while self.unvisited_list:

            for edge in vertex.adjacency_list:
                if edge.target_vertex in self.unvisited_list:
                    heapq.heappush(self.edge_heap, edge)

            min_edge = heapq.heappop(self.edge_heap)

            if min_edge.target_vertex in self.unvisited_list:
                self.spanning_tree.append(min_edge)
                print("Edge added ", min_edge.start_vertex, "-", min_edge.target_vertex)
                self.full_cost += min_edge.weight
                vertex = min_edge.target_vertex
                self.unvisited_list.remove(vertex)

    def get_spanning_tree(self):
        return self.spanning_tree

    def get_cost(self):
        return self.full_cost


vertexA = Vertex("A")
vertexB = Vertex("B")
vertexC = Vertex("C")
vertexD = Vertex("D")
vertexE = Vertex("E")
vertexF = Vertex("F")
vertexG = Vertex("G")

edgeAB = Edge(2, vertexA, vertexB)
edgeBA = Edge(2, vertexB, vertexA)
edgeAE = Edge(5, vertexA, vertexE)
edgeEA = Edge(5, vertexE, vertexA)
edgeAC = Edge(6, vertexA, vertexC)
edgeCA = Edge(6, vertexC, vertexA)
edgeAF = Edge(10, vertexA, vertexF)
edgeFA = Edge(10, vertexF, vertexA)
edgeBE = Edge(3, vertexB, vertexE)
edgeEB = Edge(3, vertexE, vertexB)
edgeBD = Edge(3, vertexB, vertexD)
edgeDB = Edge(3, vertexD, vertexB)
edgeCD = Edge(1, vertexC, vertexD)
edgeDC = Edge(1, vertexD, vertexC)
edgeCF = Edge(2, vertexC, vertexF)
edgeFC = Edge(2, vertexF, vertexC)
edgeDE = Edge(4, vertexD, vertexE)
edgeED = Edge(4, vertexE, vertexD)
edgeDG = Edge(5, vertexD, vertexG)
edgeGD = Edge(5, vertexG, vertexD)
edgeFG = Edge(3, vertexF, vertexG)
edgeGF = Edge(3, vertexG, vertexF)

unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG]

vertexA.adjacency_list.append(edgeAB)
vertexA.adjacency_list.append(edgeAC)
vertexA.adjacency_list.append(edgeAE)
vertexA.adjacency_list.append(edgeAF)
vertexB.adjacency_list.append(edgeBA)
vertexB.adjacency_list.append(edgeBD)
vertexB.adjacency_list.append(edgeBE)
vertexC.adjacency_list.append(edgeCA)
vertexC.adjacency_list.append(edgeCD)
vertexC.adjacency_list.append(edgeCF)
vertexD.adjacency_list.append(edgeDB)
vertexD.adjacency_list.append(edgeDC)
vertexD.adjacency_list.append(edgeDE)
vertexD.adjacency_list.append(edgeDG)
vertexE.adjacency_list.append(edgeEA)
vertexE.adjacency_list.append(edgeEB)
vertexE.adjacency_list.append(edgeED)
vertexF.adjacency_list.append(edgeFA)
vertexF.adjacency_list.append(edgeFC)
vertexF.adjacency_list.append(edgeFG)
vertexG.adjacency_list.append(edgeGD)
vertexG.adjacency_list.append(edgeGF)

algo = PrimsJarnik(unvisited_list)

algo.calculate_spanning_tree(vertexD)

print(algo.get_cost())
