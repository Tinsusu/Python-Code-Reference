
# First exercise Read text file
file = open("Land_and_Ocean_summary.txt","r")
list_of_lines = file.readlines()
file.close()

new = []
for line in list_of_lines:
    if line[0] == "%":
        pass
    else:
        line = line.strip("\n")
        if len(line) > 1:
            new.append(line)
#print(list_of_lines,"\n") #First exercise
#print(new) #Second

#print(int(new[0][:6]))
#print(int(new[1][:6]))
#print(int(new[2][:6]),"\n")

output = []
i = 0
for i in range(0,len(new)):
    if int(new[i][:6]) >= 2000:
        output.append(new[i])
    else:
        pass
#print(output)

for result in output:
    print(result)