# A story of two collections
  # List
  # Dictionary
#https://en.wikipedia.org/wiki/Associative_array

#Dictionaries -> key value pair
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse) # {'money': 12, 'tissues': 75, 'candy': 5}

print(purse['candy']) # 3

#####################################################

#Comparing lists and dictionaries
lst = list()
lst.append(21)
lst.append(183)
print(lst) # [21, 183]
lst[0] = 23
print(lst) # [23, 183]

print('--------------------------------')
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd) # {'course': 182, 'age': 21}
ddd['age'] = 23
print(ddd) # {'course': 182, 'age': 23}

#####################################################

#Dictionary Literals (Constants)
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj) # {'jan' : 100, 'fred' : 42, 'chuck' : 1}
ooo = {}
print(ooo) # {}

#####################################################

#Counting with dictionaries

#Many counters with a dictionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc) # {'csev' : 1, 'cwen' : 1}
ccc['cwen'] = ccc['cwen'] + 1
print(ccc) # {'csev' : 1, 'cwen' : 2}

#####################################################

ccc = dict()
# print(ccc['csev']) # will fail
print('csev' in ccc) # False

#####################################################

#When we see a new name
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) # {'csev' : 2, 'cwen' : 2, 'zqian' : 1}

#--------------------------------------------------#

#The get method for dictionaries
if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)      # 0 -> default
print(name)
print(x)

#--------------------------------------------------#

#Simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#####################################################

#Dictionaries and Files
#Counting pattern
counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts: ', counts)

#####################################################

#Definite Loops and Dictionaries
counts = {'Chuck' : 1, 'Fred' : 42, 'Jan' : 100}
for key in counts:
    print(key, counts[key])

#####################################################

#Retreiving lists of Keys and Values
jjj = {'Chuck' : 1, 'Fred' : 42, 'Jan' : 100}
print(list(jjj)) # ['Chuck', 'Fred', 'Jan']
print(jjj.keys()) # ['Chuck', 'Fred', 'Jan']
print(jjj.values()) # [1, 42, 100]
print(jjj.items()) # [('Chuck', 1), ('Fred', 42), ('Jan', 100)] -> What is a tuple? Coming soon...

#####################################################

#Bonus: Two iteration variables
jjj = {'Chuck' : 1, 'Fred' : 42, 'Jan' : 100}
for key, value in jjj.items():
    print(key, value)

#####################################################

name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = None
bogWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord, bigCount)

#####################################################

fname = input('Enter file name:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        #print(w)
        if w in di:
            di[w] += 1
        else:
            di[w] = 1
        #print(w, di[w])
print(di)

#------------------------------------------#

fname = input('Enter file name:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        #print(w)
        # Idiom : retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
        #print(w, di[w])
print(di)

#Now we want to find the most common word
largest = -1
for k, v in di.items():
    if v > largest:
        largest = v
        mcw = k
print('The most common word:', mcw, largest)
