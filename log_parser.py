#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-03-20 01:46:28
# @Last Modified by:   Ivan Zemlyaniy
# @Last Modified time: 2015-06-23 22:33:12

#This program read file given as link as argument in comand line
#(https://dl.dropboxusercontent.com/u/1397435/mbox-short.txt)
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines
#as the person who sent the mail.


from sys import argv
from urllib2 import urlopen

try:
    logfile = urlopen(argv[1])

except ValueError:  # invalid URL
    logfile = open(sys.argv[1])

def email_count(logfile):
""" Function for counting emails inside log file
"""
    count = {}
    bigcount = None
    mostmail = None

    for line in logfile: #parsing file and makinng dictionary with counter
        if not line.startswith("From:") : continue
        line = line.split()
        mail = line[1]
        count[mail] = count.get(mail,0) + 1

    for mail,counts in count.items(): #defining of biggest count mail
        if bigcount is None or counts > bigcount :
            mostmail = mail
            bigcount = counts

    print mostmail, bigcount

if __name__ == "__main__":
    email_count(logfile)
