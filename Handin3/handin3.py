
import re
def read_word_file(filename):
    '''
    The function should open the file, iterate over the lines,
    and remove the new lines at the end of each line.
    :param filename:
    :return: a list of  a tuple consisting of two values:
    the line number (starting at zero), and the line string (without newlines)
    '''
    file = open(filename,"r")
    list_of_lines = file.readlines()
    file.close()
    data_list = []
    for number,line in enumerate(list_of_lines):
        line = line.strip("\n")
        data_list.append((number,line))  #append tuple into datalist
    return data_list

#print(read_word_file("british-english")[0:5])

def read_word_file2(filename,filter_re_str=""):

    """ function  compiles this filter_re_str into a regular expression,
    and then use this regular expression to search in each
    line whether it can find a match of the regular expression in the line
    :param filename and filter_re_str
    """
    pattern = re.compile(filter_re_str)
    print(len(filter_re_str))
    print(filter_re_str)
    file = open(filename, "r")
    list_of_lines = file.readlines()
    file.close()
    data_list = []
    for number, line in enumerate(list_of_lines):
        line = line.strip("\n")
        data_list.append((number, line))  # append tuple into datalist
    #return data_list
    filter_list = []
    for data in data_list:
        if len(filter_re_str) > 0:
            if re.search(pattern,data[1]):
                filter_list.append(data)
        else:
            filter_list.append(data)
    return filter_list

#print(read_word_file2(filename='british-english'))
#print(read_word_file2(filename='british-english', filter_re_str="^py[A-Za-z]{4}$"))