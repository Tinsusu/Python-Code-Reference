number_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20\n"
number_str_cleaned = number_str[:-1]
print(number_str_cleaned)

number_str_list = number_str_cleaned.split(" ")
print(number_str_list)

for number in number_str_list:
  print(number)
