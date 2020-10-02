# """
# Input string of words separated by spaces
# Words should appear in same order but no duplicates
# No extra spaces at end of string (.trim())

# Cannot use set because set are unordered and unindexed
# Cannot use dictionaries because unordered

# Can use list or tuple ???
# Pseudocode:
# Step 1: Split input sentence separated by space into words.
# Step 2: So to get all those strings together first we will join each string in a given list of strings.
# Step 3: now create a dictionary using the counter method which will have strings as key and their Frequencies as value.
# Step 4: Join each words are unique to form single string.

# """
from collections import OrderedDict


def no_dups(s):
#     # Your code here
    return " ".join(OrderedDict.fromkeys(s)




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
