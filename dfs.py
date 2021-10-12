class Node:

    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjacency_list = []
        self.predecessor = None


class DFS:

    def dfs(self, node):

        node.visited = True

        print(node.data)

        for v in node.adjacency_list:
            if not v.visited:
                self.dfs(v)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

dfs = DFS()
dfs.dfs(node1)
