# Function to determine if a string contains three consecutive double lectures
# It has been switched slightly to use a for loop instead of a while loop.
def two_double(s):
    for i in range(0, len(s)-3):
        if s[i] == s[i+1] and s[i+2] == s[i+3]:
            return True
    return False

# Function to read and apply the three_double test to each string in
# an input file.  It counts the number of results.
def find_two_double(fin):
    count = 0
    for w in fin:
        w = w.strip().strip('\n')
        if two_double(w):
            print w
            count = count + 1
    if count == 0:
        print '<None found>'
    else:
        print count, 'found'

################################################

# Bring in a package to access files over the web
import urllib

import subprocess

# Access the file containing the valid letters
words_url = "http://thinkpython.com/code/words.txt"
words_file = urllib.urlopen(words_url)
# words_file = open('words.txt')

# Apply the actual test
find_two_double(words_file)

mario = "/Users/hsartoris/Documents/Programming/python/Python 2.7 test/preview.mp3"
return_code = subprocess.call(["afplay", mario])