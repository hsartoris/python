# Function to determine if a string contains three consecutive double lectures
# It has been switched slightly to use a for loop instead of a while loop.
def three_double(s):
    for i in range(0, len(s)-5):
        if s[i] == s[i+1] and s[i+2] == s[i+3] and s[i+4] == s[i+5]:
            return True
    return False

# Function to read and apply the three_double test to each string in
# an input file.  It counts the number of results.
def find_three_double(fin):
    count = 0
    for w in fin:
        w = w.strip().strip('\n')
        if three_double(w):
            print w
            count = count + 1
    if count == 0:
        print '<None found>'
    else:
        print count, 'found'

################################################

# Bring in a package to access files over the web
import urllib

# Access the file containing the valid letters
words_url = "http://thinkpython.com/code/words.txt"
words_file = urllib.urlopen(words_url)
# words_file = open('words.txt')

# Apply the actual test
find_three_double(words_file)
