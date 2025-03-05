import handin4
wordlist_british = (handin4.wordfile_to_list("british-english"))
#print(len(wordlist_british))

wordlist_american = (handin4.wordfile_to_list("american-english"))
#print(len(wordlist_american))

#for question2

import timeit
start_time = timeit.default_timer()
differences_linear_search = (handin4.wordfile_differences_linear_search("british-english","american-english"))
time_spent = timeit.default_timer() - start_time
time_spent_linear_search = time_spent
#print(f"Time spent for linear search: {time_spent_linear_search}")
#print(len(differences_linear_search))

#for question3

start_time = timeit.default_timer()
differences_binary_search = handin4.wordfile_differences_binary_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
time_spent_binary_search = time_spent
#print(f" Binary time: {time_spent_binary_search}")
#print(len(differences_binary_search))
#print(f" linear search spent longer: {time_spent_linear_search/time_spent_binary_search}")


#for question 4

worddict_american = handin4.wordfile_to_dict("american-english")
#print(f"Word dict american:{worddict_american}")

#for question 5

start_time = timeit.default_timer()
differences_dict_search = handin4.wordfile_differences_dict_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
time_spent_dict_search = time_spent
#print(f"Dictionart search time: {time_spent_dict_search}")
#print(f"Diferrent dict search: {differences_dict_search}")
#print(len(differences_dict_search))
#print(f" linear search spent longer: {time_spent_linear_search/time_spent_dict_search}")