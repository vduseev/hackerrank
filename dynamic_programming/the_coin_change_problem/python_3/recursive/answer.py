#!/bin/python3

import sys

desired_value, amount_of_coins = input().strip().split(' ')
desired_value, amount_of_coins = [int(desired_value), int(amount_of_coins)]
coins = list(map(int, input().strip().split(' ')))
coins.sort()
print(coins, file=sys.stderr)

memo = {}


def T(m, n):
    """
    Approach 6:
    Recursion basis: T(m,n<=0) = 1; T(0,n>0) = 0;
    Indicator function: i = { 1 if n%v > 0 else 0 };
    T(m,n) = T(m-1,n) + i*T(m,n-i*v)
    """

    if (m, n) in memo:
        # value is already memoized
        # take it from memory
        t = memo[m, n]
    else:
        # value is not memoized
        # compute it
        if n <= 0:
            # basis of recursion
            t = 1
        elif m == 0 and n > 0:
            # another basis of recursion
            t = 0
        else:
            # value of current coin under index m
            v = coins[m - 1]
            # indicator function - returns 1 if this coins fits 1 or more times into current desired value of n
            i = 1 if n // v > 0 else 0
            # recursion
            t = T(m - 1, n) + i * T(m, n - v)
        # save calculated value into memo
        memo[m, n] = t
    return t

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = T(amount_of_coins, desired_value)
print(ways)
