# miZpel

Check if a word is spelled correctly and get a list of suggested words if it is not. <br />

# Firs install the package
 - explain how to do it... <br />

# Then import the main module
from WordDictionary import WordDictionary <br />

# Instanciate an object of the dictionary
  `wd = WordDictionary()` <br />
  - You may also pass in the name of your own text file dictionary or choose one of the built in ones <br />
  - remember to add the file to ???? <br />
  `wd = WordDictionary("my_dictionary.txt")` <br />

# Check if a word exists in the dictionary
As simple as: <br />
  `if "mizpel" in wd:` <br />

# Check if a word does not exist and get a list of similar words
As simple as: <br />
  `if "mizpel" not in wd:` <br />
  &nbsp; &nbsp; `similar_words = wd.get_similar_words("mizpel")` <br />

# Main features:
  - Add your own words <br />
    `wd.append("mizpel")` <br />
    (it returns True if it does not alreay exist and was added or False otherwise) <br />
    
  - Remove words <br />
    `wd.remove("mizpel")` <br />
    (it returns True if it does exists and was removed or False otherwise) <br />

  - The more you use it the faster it becomes <br />
    - when you get suggestions for misspelled words the list returned is saved for future reference and results come much, much faster!!! <br />

# Dictionary options
- file names, characteristics and credits <br />
