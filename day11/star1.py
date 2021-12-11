import os
import numpy as np
import copy
from scipy import signal

def parse_rules(fname):
    octo_list = []
    for line in open(fname):
        print(line)
        line = line.strip()
        octos = [int(octo) for octo in line]
        octo_list.append(octos)
    return np.array(octo_list)

def do_step(octo_array):
    octo_array += 1
    flashers = octo_array > 9
    new_flashers = flashers.copy()
    num_flashers = sum(flashers.flatten().astype(int))
    flash_kernel = np.ones((3, 3))
    flash_kernel[1,1] = 0 # don't think this is strictly necessary, we'll see
    while sum(new_flashers.flatten().astype(int)) > 0:
        this_flash = signal.convolve2d(new_flashers, flash_kernel, mode='same')
        octo_array = (octo_array + this_flash)*(~flashers)
        new_flashers = octo_array > 9
        num_flashers += sum(new_flashers.flatten().astype(int))
        flashers += new_flashers
    return num_flashers, octo_array



def main():
    octo_array = parse_rules('input.txt')
    num_steps = 100
    total_flashen = 0
    for _ in range(num_steps):
        num_flash_in_step, octo_array = do_step(octo_array)
        total_flashen += num_flash_in_step
    print('total flashen = ', total_flashen)



if __name__== main():
    main()