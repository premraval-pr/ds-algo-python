import sys
import heapq


class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:

    def __init__(self, data):
        self.data = data
        self.min_distance = sys.maxsize
        self.adjacency_list = []
        self.predecessor = None
        self.visited = False

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        return self.min_distance < other.min_distance


class Algorithm:

    @staticmethod
    def calculate_shortest_path(start_vertex):

        q = []
        start_vertex.min_distance = 0
        heapq.heappush(q, start_vertex)

        while q:
            actual_vertex = heapq.heappop(q)

            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                temp_distance = u.min_distance + edge.weight

                if temp_distance < v.min_distance:
                    v.min_distance = temp_distance
                    v.predecessor = u
                    heapq.heappush(q, v)

    @staticmethod
    def get_shortest_path(target_vertex):

        print("Shortest path cost to the vertex is: ", target_vertex.min_distance)

        node = target_vertex

        while node:
            print(node.data)
            node = node.predecessor


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')
node_G = Node('G')
node_H = Node('H')

edge_AB = Edge(5, node_A, node_B)
edge_AH = Edge(8, node_A, node_H)
edge_AE = Edge(9, node_A, node_E)
edge_BD = Edge(15, node_B, node_D)
edge_BH = Edge(4, node_B, node_H)
edge_BC = Edge(12, node_B, node_C)
edge_EH = Edge(5, node_E, node_H)
edge_EF = Edge(4, node_E, node_F)
edge_EG = Edge(20, node_E, node_G)
edge_HC = Edge(7, node_H, node_C)
edge_HF = Edge(6, node_H, node_F)
edge_CD = Edge(3, node_C, node_D)
edge_CG = Edge(11, node_C, node_G)
edge_FC = Edge(1, node_F, node_C)
edge_FG = Edge(13, node_F, node_G)
edge_DG = Edge(9, node_D, node_G)

node_A.adjacency_list.append(edge_AB)
node_A.adjacency_list.append(edge_AE)
node_A.adjacency_list.append(edge_AH)
node_B.adjacency_list.append(edge_BC)
node_B.adjacency_list.append(edge_BD)
node_B.adjacency_list.append(edge_BH)
node_H.adjacency_list.append(edge_HC)
node_H.adjacency_list.append(edge_HF)
node_E.adjacency_list.append(edge_EF)
node_E.adjacency_list.append(edge_EG)
node_E.adjacency_list.append(edge_EH)
node_D.adjacency_list.append(edge_DG)
node_F.adjacency_list.append(edge_FC)
node_F.adjacency_list.append(edge_FG)
node_C.adjacency_list.append(edge_CD)
node_C.adjacency_list.append(edge_CG)

Algorithm.calculate_shortest_path(node_A)
Algorithm.get_shortest_path(node_D)
