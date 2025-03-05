
#Branching exercise
import random
x = random.randint(1,6)
print("The result of your dice:",x,"\n")
#ifelse is today the first one does not workout thou

##### Exercise
"""" Lists — exercise
Create a variable containing the following string:
Horse sense is the thing a horse has which keeps it
from betting on people. W.C. Fields
1.Convert this string to a list of words.
2.Find the index of the word ”Horse” in the sequence.
3.Sort the list.
4.Print out the first 3 elements of this sorted list.
Bonus exercise: Try to reverse the list of words using the slice operation."""

st = "Horse sense is the thing a horse has which keeps it from betting on people. W.C. Fields"
new_st = st.split(" ")
print(new_st)
print("Index of the word horse::: ",st.find("Horse"))  #find for string but for the list we use index function

print("Show the new sorted list:::\n",sorted(new_st)) #sorted doest not workt with new_st.sort()

# this will change new.st  but the function sorted will create a copy for you.

print("Print out the first 3 elements of this sorted list\n",sorted(new_st)[:3])

#Reverse List
re = new_st[::-1] #not specify the first and the last but set a step of -1
print(" Reverse the list of words:::: \n",re)

""" Loops - exercise
Create the following list: [6,9,4,8,7,1,2].
Write a while loop that prints each element in the list.
Write a for loop that prints each element in the list.
Write a loop that prints all elements that are larger than their left neighbour (for the above example: 9, 8, 2). Which type of loop is best suited for this purpose?
"""

num = [6,9,4,8,7,1,2]
#while loop to printout all numbers
i = 0
while i < len(num):
    print(num[i])
    i += 1

#forloop
for n in num:
    print("From forloop: ",n)

for i in range(len(num)):
    value = num[i]
    if i > 0 and num[i] > num[i-1]:
        print(value)