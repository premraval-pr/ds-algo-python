class Vertex:

    def __init__(self, data):
        self.data = data
        self.node = None


class Node:

    def __init__(self, height, node_id, parent_node):
        self.height = height
        self.node_id = node_id
        self.parent_node = parent_node


class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet:

    def __init__(self, vertices):
        self.vertices = vertices
        self.root_nodes = []
        self.node_count = 0
        self.set_count = 0
        self.make_sets(vertices)

    def make_sets(self, vertices):
        for v in vertices:
            self.make_set(v)

    def make_set(self, v):
        node = Node(0, len(self.root_nodes), None)
        v.node = node
        self.root_nodes.append(node)
        self.set_count += 1
        self.node_count += 1

    def find(self, node):
        current_node = node
        while current_node.parent_node:
            current_node = current_node.parent_node

        root = current_node

        current_node = node

        while current_node is not root:
            temp = current_node.parent_node
            current_node.parent_node = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.height < root2.height:
            root1.parent_node = root2
        elif root2.height < root1.height:
            root2.parent_node = root1
        else:
            root2.parent_node = root1
            root1.height = root1.height + 1


class KruskalAlgorithm:

    @staticmethod
    def spanning_tree(vertices, edges):

        disjoint_sets = DisjointSet(vertices)
        spanning_trees = []

        edges.sort()

        for edge in edges:
            u = edge.start_vertex
            v = edge.target_vertex

            if disjoint_sets.find(u.node) is not disjoint_sets.find(v.node):
                spanning_trees.append(edge)
                disjoint_sets.merge(u.node, v.node)

        for edge in spanning_trees:
            print(edge.start_vertex.data, " - ", edge.target_vertex.data)


vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)

vertex_list = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]

edge_list = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]

KruskalAlgorithm.spanning_tree(vertex_list, edge_list)
