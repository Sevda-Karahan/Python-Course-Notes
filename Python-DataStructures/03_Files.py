# Files #

# Opening File
# Using open()
fhand = open('mbox.txt', 'r')
print(fhand)

############################################################

#The newline character
stuff = 'Hello\nWorld!'
print(stuff)

stuff = 'X\nY'
print(stuff)

print(len(stuff)) # 3

############################################################

# Processing Files #
#File handle as a sequence
xfile = open('mbox.txt', 'r')
for cheese in xfile:
    print(cheese)

############################################################

#Counting lines in a file
fhand = open('mbox.txt', 'r')
count = 0
for line in fhand:
    count += 1
print('Line count:', count)

############################################################

# Reading the whole file
fhand = open('mbox-short.txt', 'r')
inp = fhand.read()
print(len(inp))
print(inp[:6])
print(inp[:20])

############################################################

# Searching through a file
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        
############################################################

#Skipping with continue
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        continue
    print(line)

############################################################

#Using in to select lines
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

############################################################

# Prompt for file name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)

############################################################

# Bad file names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File', fname, 'cannot be opened')
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
