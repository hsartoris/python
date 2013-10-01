'''
Created on Sep 16, 2013

@author: hsartoris
'''

from array import array

def countLetter(s, c):
    count = 0
    for i in s:
        if i == c or i == c.upper():
            count += 1
    return count

def removeLetter(s, c):
    output = ""
    for i in s:
        if i != c and i != c.upper():
            output += i
    return output

inputString = raw_input("Enter a string: ")
print "String : " + inputString

vowelCount = 0
extraneousSpaces = len(inputString) - len(inputString.strip())

vowels = array('c', ['a','e','i','o','u'])

for c in vowels:
    vowelCount += countLetter(inputString, c)
    
spaceCount = countLetter(inputString, " ")
consonantCount = len(inputString) - (vowelCount + spaceCount)


consonants = removeLetter(removeLetter(removeLetter(removeLetter(removeLetter(removeLetter(inputString, ' '), 'a'), 'e'), 'i'), 'o'), 'u')


print "Vowels                     : " + str(vowelCount)
print "Consonants                 : " + str(consonantCount)
print "Spaces                     : " + str(spaceCount)
print "Spaces at beginning and end: " + str(extraneousSpaces)
print "Consonants only            : " + consonants