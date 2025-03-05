
import numpy as np
import random
def count_larger_than_neighbor_without_loops(list_of_numbers):
    """ Count larger than neighbor without loops"""
    arr = np.array(list_of_numbers)     # use numpy.split() function #use reverse function
#    arr2 = np.split(arr, len(arr) / 2)
#    ar = np.array(arr2)
#    a = ar.argmax(axis=1)
    arr = arr[::-1]
    result = np.diff(arr)
    result[result < 0] = 0
    result[result > 0] = 1
    return np.sum(result)

#print(count_larger_than_neighbor_without_loops([6,9,4,8,7,1,2]))

#2
def read_mnist_csv(filename):
    ''' this function read file and return a numpy array numpy array'''
    x1 = np.genfromtxt(filename, delimiter = ",",skip_header= 1)
    return x1


#print(read_mnist_csv("mnist_test_200.csv"))
#3
def group_by_label(n):
    """ Group the data by labels.
    The out put should be in 10 elements
    """
    data_label = []
    for i in range(10):
        a = n[n[:,0] == i]
        data_label.append(a)
    return data_label

#x=read_mnist_csv("mnist_test_200.csv")
#digit_image_groups = group_by_label(x)
#print(digit_image_groups)
#print(digit_image_groups.shape)
# Question 4
def get_image(digit_image_groups, digit):
    """  choose a random image, which should then
    be returned to the user as a 28x28 numpy array """
    x = random.randint(0, digit_image_groups[digit].shape[0]-1)
    output = digit_image_groups[digit][x][1:].reshape(28,28)
    return output


