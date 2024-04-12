import Ex_25 as ex

sentence = "All good things come to those who wait."
words = ex.break_words(sentence)
print(words)
sorted_words = ex.sort_words(words)
print(sorted_words)
ex.print_first_word(words)
ex.print_last_word(words)
print(words)
ex.print_first_word(sorted_words)
ex.print_last_word(sorted_words)
print(sorted_words)
