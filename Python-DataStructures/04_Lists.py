# Lists
# A list is a kind of collection
friends = ['Joseph', 'Glenn', 'Sally'] # a list of strings
carryon = ['socks', 'shirt', 'perfume'] # a list of strings

####################################################################

# List constants
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])
print([])

####################################################################

# We already used lists
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

####################################################################

# Lists and definite loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year', friend)
print('Done!')

#Looking inside lists
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

####################################################################

"""
#Strings are immutable
fruit = 'Banana'
fruit[0] = 'b'
"""

####################################################################

#Lists are mutable
lotto = [2, 14, 26, 41, 63]
print(lotto)

lotto[2] = 28
print(lotto)

####################################################################

greet = 'Hello Bob'
print(len(greet))

####################################################################

#How long is a List?
x = [1, 2, 'joe', 99]
print(len(x)) # 4

####################################################################

# Using the range function (The range function returns a list of numbers)
print(range(4)) # range(0, 4) -> [0, 1, 2, 3]
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends))) # range(0,3) -> [0, 1, 2]
# print(type(range(4))) -> <class 'range'>

####################################################################

#A tale of two loops
friends = ['Joseph', 'Glenn', 'Sally']
# 1
for friend in friends:
    print('Happy new year', friend)
# 2
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year', friend)

#Manipulating Lists#
####################################################################

#Concatenating Lists Using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

####################################################################

#Lists can be sliced using :
t = [9, 41, 12, 3, 74, 15]
print(t[1:3]) # [41, 12]
print(t[:4]) # [9, 41, 12, 3]
print(t[3:]) # [3, 74, 15]
print(t[:]) # [9, 41, 12, 3, 74, 15]
print(t) # [9, 41, 12, 3, 74, 15]

####################################################################

"""
#List Methods
x = list()
type(x) # <type 'list'>
dir(x)

#https://docs.python.org/3/tutorial/datastructures.html
"""
####################################################################

#Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) # ['book', 99]
stuff.append('cookie')
print(stuff) # ['book', 99, 'cookie']

####################################################################

#Is something in a list
some = [1, 9, 21, 10, 16]
9 in some # True
15 in some # False
boolean = 20 not in some  # True
print(boolean) # True

####################################################################

#Lists are in order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends) # ['Glenn', 'Joseph', 'Sally']
print(friends[1]) # Joseph

####################################################################

#Built-in functions and lists
nums = [3, 41, 12, 9, 74, 15]
print('len:', len(nums)) # 6
print('max:', max(nums)) # 74
print('min:', min(nums)) # 3
print('sum:', sum(nums)) #154
print('average:', sum(nums)/len(nums)) # 25.6

####################################################################

#Calculating average
#In Earlier chapters, we did it like that:
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count += 1
average = total / count
print('Average:', average)

print('--------------------------------')
#Now, another approach using list:
numList = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numList.append(value)
average = sum(numList) / len(numList)
print('List:', numList)
print('Average:', average)

#Lists and strings
####################################################################

#Best Friends: String and Lists
abc = 'With three words'
stuff = abc.split()
print(stuff) # ['With', 'three', 'words']
print(len(stuff)) # 3
print(stuff[0]) # With

print('--------------------------------')
print(stuff) # ['With', 'three', 'words']
for w in stuff:
    print(w)

####################################################################

line = 'A lot                   of spaces'
etc = line.split()
print(etc) # ['A', 'lot', 'of', 'spaces']

####################################################################

# split() with delimeter 
line = 'first;second;third'
thing = line.split()
print(thing) # ['first;second;third']
print(len(thing)) # 1

print('--------------------------------')
thing = line.split(';')
print(thing) # ['first', 'second', 'third']
print(len(thing)) # 3

# split() -> parceling in mail data
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print(words[1])

####################################################################
   
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words) # ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan',  '5', '09:14:16', '2008']

####################################################################

# The double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
print(email) # stephen.marquard@uct.ac.za
pieces = email.split('@') 
print(pieces) # ['stephen.marquard', 'uct.ac.za']
host = pieces[1]
print(host) # uct.ac.za

####################################################################

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.strip()
    # Guardian
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
