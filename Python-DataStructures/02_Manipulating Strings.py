# Manipulating Strings #
# String Concatenation

a = "Hello"
b = a + "There"
print(b) # HelloThere
c = a + ' ' + 'There'
print(c) # Hello There

#####################################################################

# Using in as a logical operator
fruit = 'banana'
'n' in fruit # True
print('n' in fruit) # True
'm' in fruit # False
'nan' in fruit # True

if 'a' in fruit:
    print('Found it!')

#####################################################################
# String comparison 

word = 'banana'
if word == 'banana':
    print("All right, bananas.")

#-------------------------------------------------------------------#

word = 'apple'
#word = 'banana'
#word = 'cucumber'
if word < 'banana':
    print('Your word,', word, ', comes before banana.')
elif word > 'banana':
    print('Your word,', word, ', comes after banana.')
else:
    print("All right, bananas.")

#####################################################################

# String Library 
greet = 'Hello Bob'
zap = greet.lower()
print(zap) # hello bob
print(greet) # Hello Bob

print('Hi there!'.lower()) # hi there!

#####################################################################

stuff = 'Hello world!'
type(stuff)
dir(stuff)

# https://docs.python.org/3/library/stdtypes.html#string-methods

#####################################################################

str.capitalize()
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])

str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()

#####################################################################

# Searching a string
fruit = 'banana'
pos = fruit.find('na')
print(pos) # 2

aa = fruit.find('z')
print(aa) # -1

#####################################################################

# Making everything UPPER CASE
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn) # HELLO BOB

www = greet.lower()
print(www) # hello bob

#####################################################################

# Search and replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr) # Hello Jane

nstr = greet.replace('o', 'X')
print(nstr) # HellX BXb

#####################################################################

# Stripping Whitespace
greet = '  Hello Bob    '
greet.lstrip() # 'Hello Bob    '
#print(greet.lstrip()) # 'Hello Bob    '
greet.rstrip() # '  Hello Bob'
#print(greet.rstrip()) # '  Hello Bob'
greet.strip() # 'Hello Bob'
#print(greet.strip()) # 'Hello Bob'

#####################################################################

# Prefixes
line = 'Please have a nice day'
line.startswith('Please') # True
line.startswith('P') # True
#print(line.startswith('P'))    # True
line.startswith('p') # False

#####################################################################

# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # 21

sppos = data.find(' ', atpos)
print(sppos) # 31

host = data[atpos+1 : sppos]
print(host) # uct.ac.za

#--------------------------------------------------------------------#

str = 'X-DSPAM-Confidence: 0.8475 '

atpos = str.find(' ')
print(atpos) # 19

sppos = str.find(' ', atpos+1)
print(sppos) # 26

snum = str[atpos+1 : sppos]
fnum = float(snum)
print(fnum) # 0.8475

#--------------------------------------------------------------------#

str = 'X-DSPAM-Confidence: 0.8475 '
ipos = str.find(':')
print(ipos) # 18
piece = str[ipos+1:]  # 0.8475 ,    (or piece = str[ipos+2:] #0.8475)
print(piece) # 0.8475
value = float(piece)
print(value) #0.8475
