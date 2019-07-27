import datetime
from WordDictionary import WordDictionary


if __name__ == "__main__":
  test_words = ['bluber', 'agnostyc', 'hopelesslly', 'zoro', 'myopy',
                'miopy', 'flowr', 'flower', 'klower', 'floewr', 'flowre',
                'shavel', 'tre']

  # investigate why floewr does not bring any results.

  # Using the WordDictionary class
  wd = WordDictionary()
  # wd = WordDictionary("wlist_match5.txt")
  # wd = WordDictionary("words_alpha.txt")

  for word in test_words:
    start = datetime.datetime.now()
    similar_words = []
    if word not in wd:
      similar_words = wd.get_similar_words(word)
    else:
      print(f'{word} is in the dictionary')
    end = datetime.datetime.now()
    print(f'It took {end-start} milliseconds to search {word}: {similar_words}')

  print(f'\nadding miopy: {wd.append("miopy")}')
  print(f'adding miopy again: {wd.append("miopy")}')
  print(f'is miopy in wd: {"miopy" in wd}')
  print(f'removing miopy: {wd.remove("miopy")}')
  print(f'is miopy in wd: {"miopy" in wd}')

  print("\n2nd round.")
  for word in test_words:
    # print(f'\nFinding similar words to {word}...')
    start = datetime.datetime.now()
    similar_words = []
    if word not in wd:
      similar_words = wd.get_similar_words(word)
    end = datetime.datetime.now()
    print(f'It took {end-start} milliseconds to search {word}: {similar_words}')
