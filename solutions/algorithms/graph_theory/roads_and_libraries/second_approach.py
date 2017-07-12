class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, from_node, to_node):


q = int(input().strip())
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]