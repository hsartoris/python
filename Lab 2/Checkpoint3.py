'''
Created on Sep 2, 2013

@author: hsartoris
'''
balance = 1000
annualInterestRate = .03
depositPerMonth = 100
compoundedEvery = 12

for i in range (0,12):
    if i == 5:
        print "Balance at 6 months: " + str(balance)
        depositPerMonth = 150
        annualInterestRate = .0325
    balance += depositPerMonth
    balance += balance * (annualInterestRate / 12)
print "Balance at one year: " + str(balance)