import os
import numpy as np
import copy


def parse_line(line):
    line = line.strip()
    corner1, corner2 = line.split('->')
    x1, y1 = corner1.strip().split(',')
    x2, y2 = corner2.strip().split(',')
    
    return (int(x1), int(y1)), (int(x2), int(y2))

def parse_rules(fname):
    vertical_list = []
    horizontal_list = []
    max_x = 0
    max_y = 0
    
    for line in open(fname):
        # print(line)
        c1, c2 = parse_line(line)
        max_x = np.max((np.max((max_x, c1[0])), c2[0]))
        max_y = np.max((np.max((max_y, c1[1])), c2[1]))
        if x1 == x2:
            print('Recorded as vertical line')
            vertical_list.append([c1[0], c1[1], c2[1]])
        elif c1[1] == c2[1]:
            print('Recorded as horizontal line')
            horizontal_list.append([c1[1], c1[0], c2[0]])
    return vertical_list, horizontal_list, max_x, max_y

def order_points(coord_points):
    min_val = min(coord_points[1], coord_points[2])
    max_val = max(coord_points[1], coord_points[2])
    return min_val, max_val + 1


def main():
    vert_list, hor_list, max_x, max_y = parse_rules('day5_test.txt')
    print('Max values', max_x, max_y)
    tracking_array = np.zeros((max_y + 1, max_x + 1))
    for cl in vert_list:
        print('Vertical line', cl)
        up, down = order_points(cl)
        tracking_array[up:down, cl[0]] += 1
        print(tracking_array)
    for cl in hor_list:
        print('Horizontal line', cl)
        left, right = order_points(cl)
        tracking_array[cl[0], left:right] += 1
        print(tracking_array)
    print(np.sum(tracking_array.flatten()>1))


if __name__== main():
    main()