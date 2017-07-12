def get_ops_count(value, target_value):
    diff = abs(value - target_value)
    a_5 = diff // 5
    diff -= a_5 * 5
    a_2 = diff // 2
    diff -= a_2 * 2
    a_1 = diff
    return a_5 + a_2 + a_1


t = int(input().strip())
for t_idx in range(t):
    n = int(input().strip())
    c = input().strip().split(' ')
    c = [int(collegue) for collegue in c]

    initial_baseline = min(c)
    baselines = [initial_baseline]
    if initial_baseline - 1 >= 0 or True:
        baselines.append(initial_baseline - 1)
    if initial_baseline - 2 >= 0 or True:
        baselines.append(initial_baseline - 2)

    ops_counts = []
    for baseline in baselines:
        ops_count_for_baseline = 0
        for collegue in c:
            ops_count_for_baseline += get_ops_count(collegue, baseline)
        ops_counts.append(ops_count_for_baseline)

    ops_counts.sort()
    print(ops_counts[0])
