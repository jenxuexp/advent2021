import os
import numpy as np
import copy


def parse_rules(fname):
    for line in open(fname):
        print(line)
        line = line.strip()
        crab_locs = [int(num) for num in line.split(',')]
    return crab_locs

def get_distance_from_diff(diff_vec):
    # arithmetic sum formula: N*a + N*(N - 1) /2 * d, a is starting value (1) and d is step size (1)
    dist_vec = diff_vec + 0.5*diff_vec*(diff_vec - 1)
    return dist_vec

def main():
    crab_locs = parse_rules('input.txt')
    # Try the dumbest way possible
    min_val = min(crab_locs)
    max_val = max(crab_locs)
    all_possible_distances = np.arange(min_val, max_val)
    move_distance = np.zeros_like(all_possible_distances)
    for ind, dd in enumerate(all_possible_distances):
        move_distance[ind] = np.sum(get_distance_from_diff(np.abs(crab_locs - dd)))
    min_distance = all_possible_distances[np.argmin(move_distance)]
    
    print('Closest distance: ', min_distance)
    print('Average distance: ', np.mean(crab_locs))
    print('Total fuel used: ', min(move_distance))
if __name__== main():
    main()