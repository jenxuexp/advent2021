import numpy as np

def main():
    inputs = np.loadtxt('day1_input.txt')
    # print(inputs)
    diffs = np.diff(inputs)
    print(diffs)
    print('num above', sum(diffs>0))
    print(np.shape(inputs))

    sum_kernel = np.array([1,1,1])
    sum_array = np.convolve(inputs, sum_kernel, mode='valid')
    print('shape of sum array', np.shape(sum_array))
    print('num above convolved', np.sum(np.diff(sum_array)>0))



if __name__== main():
    main()