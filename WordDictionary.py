import strings as s


class WordDictionary:
    def __init__(self, _dictionary_file_name="words.txt"):
        self.dictionary_file_name = _dictionary_file_name
        print(self.dictionary_file_name)
        self.__word_list = []
        self.__word_count = 0
        self.__custom_word_list = []
        self.__custom_word_count = 0
        # memoized solution
        self.__similar_word_lists = {}
        self.__initialize_dictionary()

    def __initialize_dictionary(self):
        with open(self.dictionary_file_name, "r") as words_file:
            for line in words_file:
                self.__word_count += 1
                self.__word_list.append(line.rstrip())

    def __str__(self):
        return f'{self.dictionary_file_name} has {self.__word_count} words. User added: {self.__custom_word_count}.'

    def __len__(self):
        return self.__word_count

    def append(self, other):
        if other not in self.__custom_word_list and other not in self.__word_list:
            self.__custom_word_list.append(other)
            self.__custom_word_count += 1
            return True
        else:
            return False

    def __sub__(self, other):
        if other in self.__custom_word_list:
            self.__custom_word_list.remove(other)
            self.__custom_word_count -= 1
            return True
        else:
            return False

    def __contains__(self, item):
        # print(f'called contains with {item} {item in self.__word_list}')
        return item in self.__word_list or item in self.__custom_word_list

    def __getitem__(self, position):
        return self.__word_list[position]

    def get_similar_words(self, word_to_compare):
        if word_to_compare not in self.__similar_word_lists:  # using memoized solution if possible
            similar_by_1 = []
            for word in self.__word_list:
                if s.compare_similar(word_to_compare, word, 1):
                    similar_by_1.append(word)
            for word in self.__custom_word_list:
                if s.compare_similar(word_to_compare, word, 1):
                    similar_by_1.append(word)
            # at the end add the suggested word to a dictionary and return
            self.__similar_word_lists[word_to_compare] = similar_by_1

        return self.__similar_word_lists[word_to_compare]




