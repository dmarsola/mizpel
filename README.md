# challenges
Studying some complex challenges and algorithms.

strings.py -> String comparisons. 
  def compare_equal(str1, str2, case_sensitive=True):
  -> Compares if two strings are equal with the possibility of passing False as the third parameter to make it case insensitive.
  
  def compare_similar(str1, str2, off_by_tolerance=0):
  -> Compares two strings to see how similar they are. The third optional parameter (tolerance) defines how many characters
     can be different (less, more or altogether different) and still consider the strings similar enough.
  
  def find_similar(str1, strict_equal=False):
  -> The method uses a English dictionary and the methods above to return True if the dictionary contains the word passed
     (and False otherwise) as well as suggestions of similar words.
