import handin3
word_list = (handin3.read_word_file("british-english"))
print(word_list)

filter_re_str = "^py[A-Za-z]{4}$"
filtered_word_list = (handin3.read_word_file2("british-english",filter_re_str))
print(filtered_word_list)


