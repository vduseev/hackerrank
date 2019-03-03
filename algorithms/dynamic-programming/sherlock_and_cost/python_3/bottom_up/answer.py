# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input().strip())
for test in range(t):
    n = int(input().strip())
    b = list(map(int, input().split(' ')))

    # Memoization dictionary
    memo = {}

    def get_max_cost(j):
        """
        Computes 2 max possible costs for a[i] = 1 and a[i] = b[i]
        :param j: finishing index
        :return: tuple of max costs you could possibly obtain when considering elements a[i] to a[j]
        """
        memo[j] = (0, 0)

        for i in range(j - 1, -1, -1):

            max_cost_if_a_prev_is_1, max_cost_if_a_prev_is_b = memo[i+1]

            max_cost_if_a_is_1 = max(max_cost_if_a_prev_is_1, max_cost_if_a_prev_is_b + b[i + 1] - 1)

            max_cost_if_a_is_b = max(max_cost_if_a_prev_is_1 + b[i] - 1, max_cost_if_a_prev_is_b + abs(b[i] - b[i + 1]))

            memo[i] = (max_cost_if_a_is_1, max_cost_if_a_is_b)

        return memo[0]


    cost_if_a_is_1, cost_if_a_is_b = get_max_cost(n-1)
    print(max(cost_if_a_is_1, cost_if_a_is_b))
