MOD = 1000000007
ADJACENT_CITIES = 0
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
        ADJACENT_CITIES: set(),  # set of adjacent cities
        PARENT: fake_vertex_parent_id_value,  # parent node id
        IS_LEAF: fake_is_leaf_value  # is this node a leaf?
    } for city_id in range(1, n+1)}

    # Read the city map into adjacent list graph
    for i in range(n - 1):
        road_start, road_end = [int(r) for r in input().split(' ')]
        if road_start != road_end:  # Avoid loops
            # Don't forget to add road to both cities,
            # because this is an unordered graph.
            graph[road_start][ADJACENT_CITIES].add(road_end)
            graph[road_end][ADJACENT_CITIES].add(road_start)

    return graph


def transform_graph_to_rooted_tree(graph, root):
    """
    Transforms unordered graph into roted tree by selecting 'start' vertex
    as a root, and then assigning parents recursively.
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
                if len(graph[vertex][ADJACENT_CITIES] - set([vertex])) == 0:
                    graph[vertex][IS_LEAF] = True

            # Add all its children that were never visited to the stack.
            unvisited_children = graph[vertex][ADJACENT_CITIES] - visited
            stack.update(unvisited_children)
            # Record parent for these newly discovered children
            for child in unvisited_children:
                if graph[child][PARENT] is None:  # Avoid adding parent as a child's child
                    graph[child][PARENT] = vertex
    return visited


def opposite_color(color):
    if color == RED:
        return BLUE
    else:
        return RED

memo = {}


def solve_for(graph, root, color, case):
    if (root, color, case) in memo:
        return memo[root, color, case]

    if graph[root][IS_LEAF] is True:
        if case == 1:
            memo[root, color, case] = 0
            return 0
        if case == 2:
            memo[root, color, case] = 1
            return 1

    ans = 1
    invalid = 1

    for city in graph[root][ADJACENT_CITIES]:
        if city != graph[root][PARENT]:
            valid = 0
            valid += solve_for(graph, city, opposite_color(color), 1)
            invalid = invalid * valid
            valid += solve_for(graph, city, color, 2)
            ans *= valid

    if case == 1:
        ans -= invalid

    memo[root, color, case] = ans
    return ans

kingdom = scan_kingdom_map_from_input()
transform_graph_to_rooted_tree(kingdom, 1)

ans = (solve_for(kingdom, 1, RED, 1) * 2) % MOD
print(ans)
