######################### Using Python to Access Web Data ##############################

# Regular Expressions

########################################################

## Regular Expressions - PART 1 ##

# 1) Using re.search() Like find()
# find()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
#re.search()
import re

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


########################################################
        
# 2) Using re.search() Like startswith()
# startswith()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#re.search()
import re

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# Wild-Card Characters
# The dot (.) character matches any character
# The asterisk (*) character, the character is "any number of times"
#...


########################################################
        
## Regular Expressions - PART 2 ##
        
# Matching and Extracting Data
# re.search() returns a True/False depending on whether the string matches the regular expression 
# if we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) # [0-9]+ -> one or more digits       
print(y) # ['2', '19', '42']
y = re.findall('[AEIOU]+', x)
print(y) # []

# Warning: Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+', x)
print(y) # ['From: Using the :']  -> Why not ['From:'] -> Because you get the largest possible string

# Non-greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+?', x) # ? -> not greedy -> the shortest possible string
print(y) # ['From:'] 

########################################################

# Fine-tuning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x) # \S -> at least one non-whitespace character, in greedy way
print(y) # ['stephen.marquard@uct.ac.za']
y = re.findall('^From (\S+@\S+)', x) # Extract the part that is in parentheses -> (\S+@\S+)
print(y) # ['stephen.marquard@uct.ac.za']

# Remember! Extracting a host name - using find() and string slicing
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # 21

sppos = data.find(' ', atpos)
print(sppos) # 31

host = data[atpos+1 : sppos]
print(host) # uct.ac.za

# Remember! The double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
print(email) # stephen.marquard@uct.ac.za
pieces = email.split('@') 
print(pieces) # ['stephen.marquard', 'uct.ac.za']
host = pieces[1]
print(host) # uct.ac.za

# The regex version
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line) 
print(y) # ['uct.ac.za']

# Even cooler regex version
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', line) 
print(y) # ['uct.ac.za']

########################################################

# Spam Confidence 
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.strip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist)) # 0.8475 
# X-DSPAM-Confidence: 0.8475 

########################################################

# Escape Character
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y) # ['$10.00']

#https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

########################################################
