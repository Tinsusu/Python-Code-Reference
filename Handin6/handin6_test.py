import numpy as np
import pandas as pd
import handin6

df_british = pd.read_csv("british-english", keep_default_na=False, names=['word'])
#print(df_british)
#print(df_british['word'].count())
palindromes = handin6.find_palindromes(df_british)
print(handin6.find_palindromes(df_british))
print(f"palindrome_size: {handin6.find_palindromes(df_british).count()}")
matching_words = handin6.find_words_starting_with(df_british,"congra")
print(handin6.find_words_starting_with(df_british, "congra"))


#Testing data
#data = ["de","Madam","Nun","mum","madam","maam","metal","civic","Tony","Jing'''","anada's","da"]
#df = pd.DataFrame(data, columns=['word'])
#print(handin6.find_words_starting_with(df, "de"))