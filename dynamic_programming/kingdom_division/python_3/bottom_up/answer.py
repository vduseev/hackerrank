def scan_graph_from_input():
    # Read number of cities on map.
    n = int(input().strip())

    # Determine a parent for each node if we start traversing from node 1
    graph = {city_id: set() for city_id in range(1, n+1)}

    # Read the city map into adjacent list graph
    for i in range(n - 1):
        road_start, road_end = [int(r) for r in input().split(' ')]

        if road_start != road_end:  # Avoid self loops
            graph[road_start].add(road_end)
            graph[road_end].add(road_start)

    return graph


def bfs(graph, root, on_node_discovery=None, on_unvisited_children=None):
    # Queue that will be used for traversal is implemented
    # as an inverted list.
    # New nodes are added to the head of the beginning of the list.
    queue = [root]
    # Set for a faster 'not in' operation and subtraction
    visited = set()
    # Visiting order with the same length as 'visited' set, but keeps
    # the order unlike set.
    visit_order = []
    # Traverse while we have nodes to visit in the queue
    while queue:
        node = queue.pop()

        # Call user supplied function
        if on_node_discovery is not None:
            on_node_discovery(node)

        # Keep track of visited node
        visited.add(node)
        visit_order.append(node)

        # Which children of this node were not visited yet?
        unvisited_children = graph[node] - visited

        # Call user supplied function
        if on_unvisited_children is not None:
            on_unvisited_children(node, unvisited_children)

        # Add unvisited children to the queue
        queue[0:0] = unvisited_children

    return visit_order


def get_rooted_tree(graph, root):
    # Initialize rooted tree with exact same number of nodes as in the
    # supplied graph, but with richer information about each node.
    rooted_tree = {
        node_id: {
            'CHILDREN': set(),
            'PARENT': None,
            'IS_LEAF': False
        } for node_id in graph
    }

    def discover_node(node):
        parent = rooted_tree[node]['PARENT']
        parent_as_set = set() if parent is None else {parent}
        rooted_tree[node]['CHILDREN'] = graph[node] - parent_as_set

    def check_unvisited_children(node, unvisited_children):
        if unvisited_children:
            for child in unvisited_children:
                rooted_tree[child]['PARENT'] = node
        else:
            rooted_tree[node]['IS_LEAF'] = True

    visiting_order = bfs(graph, root,
                         on_node_discovery=discover_node,
                         on_unvisited_children=check_unvisited_children)

    return rooted_tree, visiting_order


def calculate_combinations(rooted_tree, visiting_order):
    # key = node_id, node_color, parent_color
    memory = {}

    # Traverse starting from the leafs and up to the root of the rooted tree
    for node_id in visiting_order[::-1]:

        # Current node is a leaf
        if rooted_tree[node_id]['IS_LEAF']:

            # Assigning value '2' to a leaf is not giving us anything, because this
            # value will not be even considered during calculation of total
            # combinations.
            # However, it is correct to state that a leaf might have 2 possible
            # colors: RED and BLUE.
            memory[node_id, 'RED', 'RED'] = 1  # parent and node have the same color
            memory[node_id, 'BLUE', 'BLUE'] = 1  # parent and node have the same color
            memory[node_id, 'RED', 'BLUE'] = 0
            memory[node_id, 'BLUE', 'RED'] = 0

        # Current node has children
        else:
            # Child combinations will be multiplied, that's why initial number is 1, not 0.
            child_combinations = 1
            red_node_combinations = 1
            blue_node_combinations = 1
            isolated_red_node_combinations = 1
            isolated_blue_node_combinations = 1
            for child_id in rooted_tree[node_id]['CHILDREN']: 
                # Assume current node is 'RED'
                red_node_combinations *= (memory[child_id, 'RED', 'RED'] + memory[child_id, 'BLUE', 'RED'])
                # Assume current node is 'BLUE'
                blue_node_combinations *= (memory[child_id, 'BLUE', 'BLUE'] + memory[child_id, 'RED', 'BLUE'])
                # Count wrong combinations
                isolated_red_node_combinations *= memory[child_id, 'BLUE', 'RED']  # current node - red, child - blue
                isolated_blue_node_combinations *= memory[child_id, 'RED', 'BLUE']  # current node - blue, child - red
            # Write down total count for 2 cases:
            # - case 1: parent of current node is of same color
            memory[node_id, 'RED', 'RED'] = red_node_combinations
            memory[node_id, 'BLUE', 'BLUE'] = blue_node_combinations
            # - case 2: parent of current node is of opposite color
            memory[node_id, 'RED', 'BLUE'] = red_node_combinations - isolated_red_node_combinations
            memory[node_id, 'BLUE', 'RED'] = blue_node_combinations - isolated_blue_node_combinations

    return memory

if __name__ == '__main__':
    # Scan graph from input
    adjacent_vertices_graph = scan_graph_from_input()
    # Declare node '1' as root
    root_id = 1
    # Transform initial graph to a rooted tree
    tree, visiting_order = get_rooted_tree(graph=adjacent_vertices_graph, root=root_id)

    # Calculate combinations
    memo = calculate_combinations(rooted_tree=tree, visiting_order=visiting_order)

    # Calculate answer for root node
    answer = (memo[root_id, 'RED', 'BLUE'] + memo[root_id, 'BLUE', 'RED']) % 1000000007

    # Give answer
    print(answer)
