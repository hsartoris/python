'''
Created on Sep 10, 2013

@author: hsartoris
'''
def framed(s):
    s_len = len(s)
    print "*"*(6 + s_len)
    print "** " + s + " **"
    print "*"*(6 + s_len)
    
s = raw_input("Enter a word to frame. \n")
framed(s)