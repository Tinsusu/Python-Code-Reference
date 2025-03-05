
#Creat list of tuples
beatles_container1 = [ ("Paul McCartney","bass guitar"),("John Lennon","rhythm guitar"),("George Harrison","lead guitar"),
("Ringo Starr","drums")]
#print(beatles_container1)
#convert tuples into dictionary
beatles_container2 = dict(beatles_container1)
#print(beatles_container2)
#print(beatles_container2['Ringo Starr'])

def beatle_lookup(name):
        if name in beatles_container2.keys():
           return beatles_container2[name]
        else:
           return "ERROR. Name '{:s}' not found. Available names: ['Paul McCartney', 'John Lennon', 'George Harrison', 'Ringo Starr']".format(name)

#print(beatle_lookup('Mick Jagger'))
#print("\n")
#print(beatle_lookup('Paul McCartney'))