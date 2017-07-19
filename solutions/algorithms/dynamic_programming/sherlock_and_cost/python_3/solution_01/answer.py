# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input().strip())
for test in range(t):
    n = int(input().strip())
    b = list(map(int, input().split(' ')))

    # Memoization dictionary
    memo = {}

    def get_max_cost(i, j):
        """
        Computes 2 max possible costs for a[i] = 1 and a[i] = b[i]
        :param i: starting index
        :param j: finishing index (included), j must be >= i
        :return: tuple of max costs you could possibly obtain when considering elements a[i] to a[j]
        """

        # First things first, check if we already computed a solution for i, j in our memoization
        # dictionary. See further for a thorough explanation of what is actually computed.
        if (i, j) in memo:
            return memo[i, j]

        # For each call of get_max_cost we basically have to consider and compare two options:
        # 1-option - current a[i] = 1
        # 2-option - current a[i] = b[i] (b[i] is a maximum possible value for a[i])
        #
        # However, before we do that comparison we need to calculate maximum possible cost
        # for all other elements starting with a[i+1] through a[j]. The recursive call will
        # return a tuple consisting of two max costs. Why two? Because the recursive call
        # will itself consider two options: a[i+1] = 1 and a[i+1] = b[i+1].
        # We will have to see which combination gives as max cost.
        #
        # Hence, amount of combinations that have to be considered is 4:
        # 1. a[i] = 1, a[i+1] = 1         => abs(1 - 1)         = 0
        # 2. a[i] = 1, a[i+1] = b[i+1]    => abs(1 - b[i+1])    = b[i+1] - 1
        # 3. a[i] = b[i], a[i+1] = 1      => abs(b[i] - 1)      = b[i] - 1
        # 4. a[i] = b[i], a[i+1] = b[i+1] => abs[b[i] - b[i+1]) = cannot be simplified
        #
        # By comparing those we will obtain 2 biggest costs, one for a[i] = 1
        # and the second is for a[i] = b[i].
        # Naturally, a root call to recursive function will also return 2
        # biggest costs for 2 cases. We will have to do a final max comparison
        # of returned values to decide which one wins.

        # What do we do if i equals j? In that case this is a single standing
        # element. We will have to return zeros for the values of max cost.
        if i == j:
            memo[i, j] = (0, 0)
            return 0, 0

        # Make a recursive call to compute biggest costs for elements from i+1 to j
        max_cost_if_a_prev_is_1, max_cost_if_a_prev_is_b = get_max_cost(i + 1, j)

        # Compute max cost if a[i] = 1
        # This covers cases 1 and 2.
        #
        # The computation below is a quite misleading one. What it actually does is a comparison
        # between 2 possible results when considering cases 1 and 2.
        # case 1:
        #   given: a[i] = 1, a[i+1] = 1
        #   cost = max_cost_if_a_prev_is_1 + abs(a[i] - a[i+1])
        #        = max_cost_if_a_prev_is_1 + abs(1 - 1)
        #        = max_cost_if_a_prev_is_1
        # case 2:
        #   given: a[i] = 1, a[i+1] = b[i+1]
        #   cost = max_cost_if_a_prev_is_b + abs(a[i] - a[i+1])
        #        = max_cost_if_a_prev_is_b + abs(1 - b[i+1])
        #        = max_cost_if_a_prev_is_b + b[i + 1] - 1
        max_cost_if_a_is_1 = max(max_cost_if_a_prev_is_1, max_cost_if_a_prev_is_b + b[i + 1] - 1)

        # Compute max cost if a[i] = b[i]
        # This covers cases 3 and 4.
        #
        # Same logic as for the cases 1 and 2 is applied here. Just a simplified equation.
        max_cost_if_a_is_b = max(max_cost_if_a_prev_is_1 + b[i] - 1, max_cost_if_a_prev_is_b + abs(b[i] - b[i + 1]))

        # Now, as we computed 4 cases and took best results for a[i] = 1 and a[i] = b[i],
        # we can return both of these biggest costs to the parent caller. But first, we
        # need to memoize the solution for this pair of i, j
        memo[i, j] = (max_cost_if_a_is_1, max_cost_if_a_is_b)
        # Return the value
        return max_cost_if_a_is_1, max_cost_if_a_is_b

    # Make a root call to recursive function.table
    cost_if_a_is_1, cost_if_a_is_b = get_max_cost(0, n-1)
    print(max(cost_if_a_is_1, cost_if_a_is_b))