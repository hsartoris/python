'''
Created on Sep 10, 2013

@author: hsartoris
'''
def framed(firstName, lastName):
    lastName += "!"
    hello = "Hello,"
    maxLength = len(hello)
    if len(firstName) > maxLength:
        maxLength = len(firstName)
    if len(lastName) >= maxLength:
        maxLength = len(lastName)
    
    helloSpaces = maxLength - len(hello)
    firstNameSpaces = maxLength - len(firstName)
    lastNameSpaces = maxLength - len(lastName)
    
    
    
    print "*"*(6 + maxLength)
    printLine(hello, helloSpaces)
    printLine(firstName, firstNameSpaces)
    printLine(lastName, lastNameSpaces)
    print "*"*(6 + maxLength)
    
def printLine(s, spaces):
    print "** " + " "*(spaces/2) + s + " "*(spaces - (spaces/2)) + " **"
    
    
firstName = raw_input("Enter your first name. \n")
lastName = raw_input("Enter your last name. \n")
framed(firstName, lastName)