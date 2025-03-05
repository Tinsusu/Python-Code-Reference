
def find_palindromes (word_dataframe, minimum_length = 4):
    """ This function will find palindromes
      Result: 1.words that are parlindromes
              2.The minimum length is 4 character"""
#    print(word_dataframe)
    mask1 = word_dataframe['word'].str.len() >= minimum_length
#    print(word_dataframe[mask1])
#    word_dataframe['word'] = word_dataframe['word'].str.upper()  # change all to upper so no case-sensitive
    mask2 = word_dataframe['word'].str[::].str.upper() == word_dataframe['word'].str[::-1].str.upper()
#    print(mask2)
    mask3 = ~word_dataframe['word'].str.contains("'")
#    mask3 = (word_dataframe['word'].str.contains("'") == False can do it this way too
#   word_dataframe['word'] = word_dataframe['word'].str.replace("'","")   #should not contain any apostrophes.
#    if word_dataframe[mask1 & mask2].count() >= 4:
    return word_dataframe[mask1 & mask2& mask3]


def find_words_starting_with(word_dataframe,prefix:str):
    """ Function will find all the word that start with prefix
        and return this match"""
    prefix = prefix.lower()
    word_dataframe['word'] = word_dataframe['word'].str.lower()
#    word_dataframe['word'] = word_dataframe['word'].str.replace("'","")  #replace apostrophes.
#    word_dataframe['new_word'] = word_dataframe['word'].str[0]  #substring for prefix
    mask4 = word_dataframe['word'].str.startswith(prefix)
    mask5 = ~word_dataframe['word'].str.contains("'")
    word_dataframe = word_dataframe.loc[mask4&mask5]
    word_dataframe = word_dataframe.assign(length=word_dataframe['word'].str.len())
#    print(word_dataframe)
    newgroup = word_dataframe.groupby(['length']).groups
    newdict={}
#loop in the dictionary to make value contains words instead of index
    for key,value in newgroup.items():
#        print(key)
        newv = []
        for x in value:
#            print(word_dataframe['word'].loc[x])
            newv.append(word_dataframe['word'].loc[x])
        newdict.update({key:newv})
    return newdict



