# miZpel

Check if a word is spelled correctly and get a list of suggested words if it is not.

# Firs install the package
 - explain how to do it...

# Then import the main module
from WordDictionary import WordDictionary

# Instanciate an object of the dictionary
  `wd = WordDictionary()` <br />
  - You may also pass in the name of your own text file dictionary or choose one of the built in ones
  - remember to add the file to ????
  `wd = WordDictionary("my_dictionary.txt")`

# Check if a word exists in the dictionary
As simple as: <br />
  `if "mizpel" in wd:`

# Check if a word does not exist and get a list of similar words
As simple as: <br />
  `if "mizpel" not in wd:` <br />
  `similar_words = wd.get_similar_words("mizpel")`
  
# Main features:
  - Add your own words <br />
    `wd.append("mizpel")` <br />
    - it returns True if it does not alreay exist and was added or False otherwise
    
  - Remove words
    `wd.remove("mizpel")`
    - it returns True if it does exists and was removed or False otherwise

  - The more you use it the faster it becomes
    - when you get suggestions for misspelled words the list returned is saved for future reference and results come much, much faster!!!

# Dictionary options
- file names, characteristics and credits