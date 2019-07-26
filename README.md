# miZpel

Check if a word is spelled correctly and get a list of suggested words if it is not.

# Firs install the package
 - explain how to do it...

# Then import the main module
from WordDictionary import WordDictionary

# Instanciate an object of the dictionary
wd = WordDictionary()
- You may also pass in the name of your own text file dictionary or choose one of the built in ones
wd = WordDictionary("my_dictionary.txt") -- add the file to ????

# Check if a word exists in the dictionary
if "mizpel" in wd:

# Check if a word does not exist and get a list of similar words
if "mizpel" not in wd:
  similar_words = wd.get_similar_words("mizpel")
  
# Main features:
  - Add your own words
    => wd.append("mizpel")
    => it returns True if it does not alreay exist and was added or False otherwise
    
  - Remove words
    => wd.remove("mizpel")
    => it returns True if it does exists and was removed or False otherwise

  - The more you use it the faster it becomes
    => when you get suggestions for misspelled words the list returned is saved for future reference and results come much, much faster!!!

# Dictionary options
- file names, characteristics and credits