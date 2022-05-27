# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# Get string inputs
word = input("Enter the first string : ")
anagram = input("Enter the second string : ")

# convert both the strings into lowercase
word = word.lower()
anagram = anagram.lower()


def find_anagram(word, anagram):
    # [assignment] Add your code here
    return sorted(word) == sorted(anagram)
    #return True
    
if find_anagram(word, anagram):
    print("Strings are anagram")
else:
    print("Strings are not anagram")
