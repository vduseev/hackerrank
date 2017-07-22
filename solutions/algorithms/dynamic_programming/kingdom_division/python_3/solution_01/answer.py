MOD = 1000000007
NEIGHBORS = 0
PARENT = 1
IS_LEAF = 2
RED = 0
BLUE = 1


def scan_kingdom_map_from_input():
    # Read number of cities on map.
    n = int(input().strip())

    # Initialize kingdom's graph map.
    #
    # Each city has a tuple of 3 values assigned to it:
    # 1 - set of adjacent cities:
    #   We are using 'set' to store a list of adjacent nodes for each city, because
    #   'set' will allow us to use efficient boolean operations when traversing
    #   the graph using DFS/BFS.
    #
    # 2 - parent city id:
    #   For this solution we are using rooted tree.
    #   -1 indicates that the parent for this vertex is not yet determined.
    #
    # 3 - boolean value indicating whether it's a leaf or not

    # Determine a parent for each node if we start traversing from node 1
    fake_vertex_parent_id_value = None
    fake_is_leaf_value = False
    graph = {city_id: {
        NEIGHBORS: set(),  # set of adjacent cities
        PARENT: fake_vertex_parent_id_value,  # parent node id
        IS_LEAF: fake_is_leaf_value  # is this node a leaf?
    } for city_id in range(1, n+1)}

    # Read the city map into adjacent list graph
    for i in range(n - 1):
        road_start, road_end = [int(r) for r in input().split(' ')]
        if road_start != road_end:  # Avoid loops
            # Don't forget to add road to both cities,
            # because this is an unordered graph.
            graph[road_start][NEIGHBORS].add(road_end)
            graph[road_end][NEIGHBORS].add(road_start)

    return graph


def transform_graph_to_rooted_tree(graph, root):
    """
    Transforms unordered graph into roted tree by selecting 'start' vertex
    as a root, and then assigning parents recursively by traversing the graph
    with DFS algorithm.
    :param graph:
    :param root:
    :return:
    """
    # Set of visited vertices is initialized as empty.
    visited = set()
    # First element in stack is the root vertex we start traversal from.
    stack = set([root])
    # We will be constantly adding children that are not visited to the
    # stack, but taking vertices that we visit out of the stack.
    while stack:
        vertex = stack.pop()
        if vertex not in visited:  # Not sure if need this condition here?

            # We just visited a new vertex
            visited.add(vertex)

            # Check if this vertex is a leaf of our tree
            if vertex != root:
                if len(graph[vertex][NEIGHBORS] - set([vertex])) == 0:
                    graph[vertex][IS_LEAF] = True

            # Add all its children that were never visited to the stack.
            unvisited_children = graph[vertex][NEIGHBORS] - visited
            stack.update(unvisited_children)
            # Record parent for these newly discovered children
            for child in unvisited_children:
                if graph[child][PARENT] is None:  # Avoid adding parent as a child's child
                    graph[child][PARENT] = vertex

    return graph


def T(m, g, node, color, is_parent_same_color):
    # Help function that returns a color opposite to the color provided
    def opposite_color(initial_color):
        if initial_color == RED: return BLUE
        else: return RED

    # If combinations for this key are already computed, then,
    # obviously, don't recompute it.
    if (node, color, is_parent_same_color) in m:
        pass

    # Leafs are the meat of these computation. They are the actual suppliers
    # of values. For each parent number of possible combinations is equal to
    # combinations_for_child_1 * combinations_for_child_2 * 2
    # But when broken down to it's base this recursion actually works with leafs.
    #
    # However, if a leaf has a color different from its parent, such
    # combination will not be acceptable. That's why we use 0 for this case.
    #
    # When leaf has same color its parent does, we consider it has 1 possible
    # value: the same value its parent has.
    elif g[node][IS_LEAF] is True:
        if is_parent_same_color is False:
            m[node, color, is_parent_same_color] = 0
        if is_parent_same_color is True:
            m[node, color, is_parent_same_color] = 1

    # Consider usual nodes with parents and children here
    else:
        current_node_combinations_count = 1
        wrong_combinations = 1

        # Get a set of neighbor nodes (children) by excluding the parent from
        # neighbor nodes set.
        child_nodes = g[node][NEIGHBORS] - set([g[node][PARENT]])

        # Consider each child
        for child_node in child_nodes:

            # First, we compute how many combinations are there for this child
            # if supply it with a parent with different color.
            #
            # The product of these possibly wrong combinations for each child
            # will have to be subtracted from final answer of current node, if
            # current node itself turns out to be surrounded by nodes of opposite color.
            #
            # Consider 2 examples (parent-to-child relationship is left-to-right;
            # current node is the one in brackets):
            #
            # 1. R -> (R) -> R -> R -> R  # that's a valid combination
            #
            # 2. R -> (B) -> R -> R -> R  # that's a wrong combinations
            #
            possibly_wrong_combinations = T(
                m, g,
                child_node,
                opposite_color(color),
                is_parent_same_color=False
            )

            # We increase the amount of all possible wrong combinations
            wrong_combinations = (wrong_combinations * possibly_wrong_combinations) % MOD

            # Second, we compute amount of combinations that are definitely valid
            # for this child, because its parent has same color
            valid_combinations = possibly_wrong_combinations + T(
                m, g,
                child_node,
                color,
                is_parent_same_color=True
            )

            # Increase the product of all valid combinations
            current_node_combinations_count = (current_node_combinations_count * valid_combinations) % MOD

        if is_parent_same_color is False:
            current_node_combinations_count = (current_node_combinations_count - wrong_combinations + MOD) % MOD

        m[node, color, is_parent_same_color] = current_node_combinations_count

    return m[node, color, is_parent_same_color]

kingdom = scan_kingdom_map_from_input()
rooted_tree = transform_graph_to_rooted_tree(kingdom, 1)

memo = {}
root_node_id = 1

answer = (T(memo, rooted_tree, root_node_id, RED, is_parent_same_color=False) * 2) % MOD
print(answer)
