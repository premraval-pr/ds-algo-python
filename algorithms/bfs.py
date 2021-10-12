class Node:

    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjacency_list = []
        self.predecessor = None


class BFS:

    @staticmethod
    def bfs(start_node):

        queue = [start_node]
        start_node.visited = True

        while queue:
            actual_node = queue.pop(0)

            print(actual_node.data)

            for v in actual_node.adjacency_list:
                if not v.visited:
                    v.visited = True
                    queue.append(v)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacency_list.append(node3)
node1.adjacency_list.append(node5)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node2)

BFS.bfs(node1)
