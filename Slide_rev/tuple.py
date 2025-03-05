t = (1,2,3,4)
print(t)   # parenthesis can be ommitted


x = 3
y = 4
print((x,y))   # Making a tuple on-the-fly

my_tuple = (1,2)    # Creating a tuple
x, y = my_tuple     # Assigning variable x to 1 and variable y to 2

print(my_tuple)

x,y = y,x      # Nice trick: swapping the values
print((x,y))   # of x and y

a = 1,2,3,4,5
print(a)

""" 
Tuples — exercise
1.Create a tuple called triplet of size 3 containing the numbers 1, 2, and 3.
2.Create three variables x, y and z and use the tuple triplet to initialize them.
3.Now create a tuple called quartet of size 4 (with the numbers 1,2,3,4), and try it again. What happens?
  ---- ValueError: too many values to unpack (expected 3)
4.Tuples support slicing. Can you use this to fix the problem?
"""

triplet = 1,2,3
x,y,z = triplet

print((x,y,z))

quartet = 1,2,3,4
print(quartet)

slice = quartet[0:3]
x,y,z = slice
print("Slice",slice)

print("Find a fix", (x,y,z))

#print("Slicing", triplet[-1])
# another trick is x,y,z,_ = quater  the _ is often used as a dummy variable.

## Dictionary
## Note the similarity to lists, except
# that individual elements are not associated with an index number, but a key.
# label for list is index but in dictionary.key is a label.
# you will get a KeyError if you use a key that doesn’t exist

days = {'Mon':'Monday', 'Tue':'Tuesday', 'Wed':'Wednesday'}
print(days['Mon'])

#how to create empty dictionary
days = {}   # empty dictionary
days['Mon'] = 'Monday'
print(days)

#delete item
del days['Mon']
print(days)
## One important difference from lists, is that dictionaries are not ordered

""" Take home message: You cannot rely on the dictionary maintaining the order in which you insert elements - you can only access them by their key.

This has changed in recent versions of Python (3.7+). They are now ordered by order of insertion.

Types: Dictionaries — operators
The only really meaningful operators for dictionaries are

==, !=, [], in
which provide the same functionality as they do in lists

Types: Dictionaries — methods
Some interesting dictionary methods:

get	Similar to [] - without key errors
items	Return list of (key,value) tuples
keys	Return list of keys
pop	Remove specified key and return value
popitem	Remove specified key and return (key,value) tuple
setdefault	Same as get, but add (key, None) if key is not already there
update	Add all elements from specified dictionary to current dictionary
values	Return list of values
>>> days.keys()
[’Tue’, ’Mon’, ’Wed’]
>>> days.pop('Wed')
’Wednesday’
>>> 'Wed' in days
False
"""
# what if the same key in a dictionary ?

""" 
Dictionaries — exercise
Create a dictionary with the keys "firstname", "lastname", and "age", and appropriate values.
Add a key named "address" to this dictionary.
Print out the list of keys in your dictionary.
Create a "name" key which as value contains a string with both your first and last names. 
Then remove the first name and last name keys. 
Can you do this without actually typing in your name again?
"""

name = {'Firstname':'Donald', 'Lastname':'Trump', 'Age':'76'}
print(name)

name['address'] = 'New York'
print("Print out the list of key:",name.keys())

## Create a "name" key which as value contains a string with both your first and last names.

name['name'] = name['Firstname'] + " " +name['Lastname']
print(name)

#Then remove the first name and last name keys.

del name['Firstname']
#del name['Lastname']

print(name)


s = "Name: %s, Height: %f" % ("Barack Obama", 1.85)
print(s)

print("I have %(n_apples)s apples and %(n_pears)s pears." % {"n_apples":5,"n_pears":7})

#String formatting - .format()
print("Name: {name}, Height: {height}".format(name="Barack Obama", height=1.85))

print("Name: {:s}, Height: {:0.1f}".format("Barack Obama", 1.85))

print("\n")

#Print format exercises

print("Name: {:s}  {:s}\nAge: {:d}".format("Barack", "Obama", 60))
print(list(range(4)))

print(("%s\n"*5)%tuple(range(5)))

s = ("%s\n"*5)%tuple(range(5))

print(type(s))

#print(("%s\n"*5) multiply string 5 times
#tuple(range(5)) creat a list and convert into tuples

# [1,2]  make it tuple tuple([1,2])