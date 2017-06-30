import math


def get_factors_of_number(n):
    factors_of_n = [1]
    if n != 1:
        factors_of_n.append(n)

    iteration = 2
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors_of_n.append(i)
            factors_of_n.append(int(n / i))
        iteration += 1

    if iteration == math.sqrt(n):
        factors_of_n.append(iteration)

    factors_of_n.sort()

    return factors_of_n


def union(sets):
    hist = {}
    for set in sets:
        for elem in set:
            if hist.get(elem) is not None:
                hist[elem] += 1
            else:
                hist[elem] = 1

    common = []
    for key in hist.keys():
        # print(key, ':', hist[key])
        if hist[key] == len(sets):
            common.append(key)

    common.sort()
    return common


def is_subset(subset, set):
    for subset_number in subset:
        if set.count(subset_number) == 0:
            return False
    return True


def get_common_factors(numbers):
    factors = []
    for number in numbers:
        factors.append(get_factors_of_number(number))

    common_factors = union(factors)
    return common_factors


def get_in_between_subset(a, b):
    x_candidates = get_common_factors(b)

    x = []
    for x_candidate in x_candidates:
        factors_of_x = get_factors_of_number(x_candidate)

        # check that A is subset of factors of X
        if is_subset(a, factors_of_x):
            x.append(x_candidate)

    return x

a = list(map(int, input('Enter the A set: ').strip().split(' ')))
b = list(map(int, input('Enter the B set: ').strip().split(' ')))

print('x:', get_in_between_subset(a, b))
