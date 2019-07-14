word_list = []
word_count = 0
with open("words.txt", "r") as words_file:
# with open("words_alpha.txt", "r") as words_file:
# with open("wlist_match5.txt", "r") as words_file:
# with open("test_words.txt", "r") as words_file:
    for line in words_file:
        word_count += 1
        word_list.append(line.rstrip())
    # word_list = words_file.read().splitlines()
    # word_list = word_list[74666:74671]
print(f'Total number of words read: {word_count}')
