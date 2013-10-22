# Function to determine if a string contains three consecutive double lectures
# It has been switched slightly to use a for loop instead of a while loop.
import string

def three_double(s):
    for i in range(0, len(s)-5):
        if s[i] == s[i+1] and s[i+2] == s[i+3] and s[i+4] == s[i+5]:
            return True
    return False

def two_double(s):
    for i in range(0, len(s) - 3):
        if s[i] == s[i+1] and s[i+2] == s[i+3]:
            return True
    return False

def startIsEnd(s):
    if (len(s) > 3 and s[0] == s[len(s) - 1]):
        return True
    return False

def fractionStartEnd(words):
    subset = 0.0
    for word in words:
        if startIsEnd(word):
            subset += 1
    return subset / len(words)

def percentContains(words, c):
    letter = 0.0
    for word in words:
        if c in word:
            letter += 1
    return letter / len(words)

def letterPercentages(words):
    percentages = []
    for c in string.ascii_lowercase:
        percentages.append(percentContains(words, c))
    return percentages

def quarterOccurrences(words):
    percentages = letterPercentages(words)
    for i in range(0, len(percentages)):
        if percentages[i] >= .25:
            print string.ascii_lowercase[i] + ": " + str(percentages[i])[:5]
    
def tenthOccurrences(words):
    percentages = letterPercentages(words)
    for i in range(0, len(percentages)):
        if percentages[i] < .1:
            print string.ascii_lowercase[i] + ": " + str(percentages[i])[:5]

def numConsecutiveDoubles(words):
    output = 0
    for word in words:
        if two_double(word):
            output += 1
    return output

def noVowels(words):
    output = []
    for word in words:
        if 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word:
            output.append(word)
    return output

def numWordsWithNoVowels(words):
    return len(noVowels(words))

def wordWith3Ys(words):
    dearthOfVowels = noVowels(words)
    for word in dearthOfVowels:
        if word.count('y') == 3:
            return word

def statistics(words):
    total = 0.0
    minLen = 2
    maxLen = 0
    for word in words:
        total += len(word)
        if len(word) < minLen:
            minLen = len(word)
        if len(word) > maxLen:
            maxLen = len(word)
    total /= len(words)
    return [total, minLen, maxLen]

def mostCommonLength(words):
    lengths = []
    stats = statistics(words)
    for i in range(stats[1], stats[2]):
        lengths.append(0)
    for word in words:
        lengths[len(word) - (stats[1] + 1)] += 1
    largest = [0,0]
    for i in range(0, len(lengths)):
        if lengths[i] > largest[1]:
            largest[0] = i
            largest[1] = lengths[i]
    return [largest[0] + stats[1] + 1, largest[1]]
        
    
# Function to apply the three_double test to each string in the words
# list.  It counts the number of results.
def find_three_double(words_list):
    count = 0
    for w in words_list:
        if three_double(w):
            print w
            count = count + 1
    if count == 0:
        print '<None found>'
    else:
        print count, 'found'

########################################################################

#  The if statement here tests to see if this is being run as a
#  program or being imported as a module.  When the value of __name__
#  is "__main__" Python is running this is the "main program".  If
#  this file had been imported as a module then the value of __name__
#  would have been "three_double" and the block of code following the
#  if would not be executed.  This establishes one of the central
#  differences between programs and modules and shows how the same
#  code may be used as a program or as a module.

if __name__ == "__main__":
    # Access the file containing the valid words
    words_file = open('words.txt')

    # Read each word, remove the white space and the \n and append it to the list
    words_list = []
    for w in words_file:
        w = w.strip().strip('\n')
        words_list.append(w)

    print "-"*20
    print "1. At least two consecutive doubles: " + str(numConsecutiveDoubles(words_list))
    print "-"*20
    print "2. Fraction of words that are longer than three and start and end with the same letter: " + str(fractionStartEnd(words_list))
    print "-"*20
    print "3. Fraction of words that contain 'e': " + str(percentContains(words_list, 'e'))[:5]
    print "   Fraction of words that contain 'z': " + str(percentContains(words_list, 'z'))[:5]
    print "-"*20
    print "4. Letters appearing in at least 25% of words: "
    quarterOccurrences(words_list)
    print "-"*20
    print "5. Letters appearing in fewer than 10% of words: "
    tenthOccurrences(words_list)
    print "-"*20
    print "6. Words with no vowels: " + str(numWordsWithNoVowels(words_list))
    #print '   Word with no vowels and three Ys: "' + wordWith3Ys(words_list) + '"'
    print "-"*20
    stats = statistics(words_list)
    print "7. Average word length: " + str(stats[0])[:4]
    print "   Minimum word length: " + str(stats[1])
    print "   Maximum word length: " + str(stats[2])
    print "-"*20
    print "8. Most common word length: " + str(mostCommonLength(words_list)[0])
    print "   Occurrences: " + str(mostCommonLength(words_list)[1])
