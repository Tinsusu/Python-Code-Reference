# First exercise Read text file
file = open("Land_and_Ocean_summary.txt","r")
list_of_lines = file.readlines()
file.close()
data_list = []
#for line in list_of_lines:
for line in list_of_lines:
    if line[0] == "%":
       continue
    else:
        line = line.strip("\n")
        if len(line) > 1:
            data_list.append(line)
# print(data_list[0])

def read_data(filename):
  file = open(filename,"r")
  list_of_lines = file.readlines()
  file.close()
  data_list = []
  for line in list_of_lines:
     if line[0] == "%":
        continue
     else:
        line = line.strip("\n")
        if len(line) > 1:
              data_list.append(line)
  return data_list

#read_data("Land_and_Ocean_summary.txt")

#year_range = (2000,2010)
def read_data2(name,year_range=(0,9999)): #default aargument should be yearrange = (negative infinite, infinite)
    file = open(name, "r")
    list_of_lines = file.readlines()
    file.close()
    data_listt = []
    for line in list_of_lines:
        if line[0] == "%":
            continue
        else:
            line = line.strip("\n")
            if len(line) > 1:
                data_listt.append(line)
    data_list2 = []
    i = 0
  #  for index, line in enumerate(data_listt):
    for i in range(0, len(data_listt)):
        if year_range[0] <= int(data_listt[i][:6]) < year_range[1]:
            data_list2.append(data_listt[i])
        else:
            pass
    #for l in data_list2:
    #    print(l)
    return (data_list2)

#print(read_data("Land_and_Ocean_summary.txt"))
#print("\n")
#print(read_data2("Land_and_Ocean_summary.txt",year_range=(2000,2002)))