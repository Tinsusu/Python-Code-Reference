
def wordfile_to_list(filename):
    """ word file into list
    :param filename:
    :return: a list of"""
    file = open(filename, "r")
    list_of_lines = file.readlines()
    file.close()
    data_list = []
    for line in list_of_lines:
        line = line.strip("\n")
        data_list.append((line))  # append tuple into datalist
    return data_list

# For question 2.
def wordfile_differences_linear_search(filename1, filename2):
    """ two lists comparison function """
    differ_ = []
    data1 = wordfile_to_list(filename1)
    data2 = wordfile_to_list(filename2)
    for word in data1:
        if word not in data2:
            differ_.append(word)
    return differ_

# For question 3
def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False

def wordfile_differences_binary_search(filename1,filename2):
    """ two lists comparison function in binaraseacrh
        return a list of the words that appear in the first file,
        but not in the second.
     """
    data1 = wordfile_to_list(filename1)
    data2 = wordfile_to_list(filename2)
    data2.sort()
    differ_ = []

    for word in data1:
        if not binary_search(data2, word):
            differ_.append(word)
    return differ_

#for question 4 we will test the speed of lookups in a Python dictionary.

def wordfile_to_dict(filename):
    """ word file into dictionary
        :param filename:
        :return: dictionary"""
    file = open(filename, "r")
    list_of_lines = file.readlines()
    file.close()
    dict_list = {}
    for line in list_of_lines:
        line = line.strip("\n")
        dict_list[line] = "None"        #append tuple into dict
    return dict_list
#print(wordfile_to_dict("british-english-test"))

#for question 5

def wordfile_differences_dict_search(filename1, filename2):
    """ compare the diferent between dict and list"""
    data1 = wordfile_to_list(filename1)
    data2 = wordfile_to_dict(filename2)
    differ_ = []
    for word in data1:
        if word not in data2:
            differ_.append(word)
    return differ_

#print(wordfile_differences_dict_search("british-english-test","american-english-test"))

#print(wordfile_differences_binary_search("british-english","american-english"))
#print(len(wordfile_differences_binary_search("british-english","american-english")))
