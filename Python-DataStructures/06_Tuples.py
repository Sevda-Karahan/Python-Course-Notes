#Tuples#
####################################################################
#Tuples are like lists (But tuples are immutable, unlike lists)
x = ('Glenn', 'Sally', 'Joseph')
print(x[2]) # Joseph
y = (1, 9, 2)
print(y) # (1, 9, 2)
print(max(y)) # 9

for iter in y:
    print(iter)

####################################################################
   
#But tuples are "immutable" 
    #Lists -> mutable
x = [9, 8, 7]
x[2] = 6
print(x) # [9, 8, 6]
    #Strings -> immutable
y = 'ABC'
#y[2] = 'D' -> will fail (Traceback)
    #Tubles -> immutable
z = (5, 4, 3)
#z[2] = 0 -> will fail (Traceback)

####################################################################

#Things not to do with Tuples
x = (3, 2, 1)
#x.sort() -> will fail (Traceback)
#x.append(5) -> will fail (Traceback)
#x.reverse() -> will fail (Traceback)

####################################################################

#A tale of two sequences
l = list()
dir(l)

t = tuple()
dir(t)

####################################################################

#Tuples are more efficient in terms of memory use and performance

####################################################################

#Tuples and Assignment
(x, y) = (4, 'Fred')
print(y) # Fred
(a, b) = (99, 98)
print(a) # 99

####################################################################

#Tuples and Dictionaries -> items() method in the dictionaries returns a list of tuples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups) # dict_items([('csev', 2), ('cwen', 4)])

####################################################################

#Tuples are Comparable
(0, 1, 2) < (5, 1, 2) # True
(0, 1, 2000000) < (0, 3, 4) # True
('Jhones', 'Sally') < ('Jhones', 'Sam') # True
('Jhones', 'Sally') > ('Adams', 'Sam') # True

####################################################################

#Sorting Lists of Tuples
d = {'a':10, 'b':1, 'c':22}
d.items() # dict_items([('a', 10), ('c', 22), ('b', 1)])
sorted(d.items()) # dict_items([('a', 10), ('b', 1), ('c', 22)])

####################################################################

#Using sorted()
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t) # [('a', 10), ('b', 1), ('c', 22)]

for (k, v) in sorted(d.items()):
    print(k, v)

####################################################################

#Sort by value Instead of Key
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for (k, v) in c.items():
    tmp.append( (v, k) )
print(tmp) #  [(10, 'a'), (22, 'c'), (1, 'b')]

tmp = sorted(tmp, reverse=True)
print(tmp) # [(22, 'c'), (10, 'a'), (1, 'b')]

####################################################################

#The top ten most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in list[:10]:
    print(key, val)

####################################################################

#Even shorter version
c = {'a':10, 'b':1, 'c':22}
print(sorted( [ (v,k) for k,v in c.items() ] , reverse=True)) # [(22, 'c'), (10, 'a'), (1, 'b')]

#List Comprehension: https://wiki.python.org/moin/HowTo/Sorting

####################################################################

#Tuples and Sorting
#Find the top 5 most common words in a file
fname = input('Enter file name:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # Idiom : retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
#print(di)

#Now we want to find the top 5 most common words
tmp = list()
for k,v in di.items():
    #print(k, v)
    newt = (v,k)
    tmp.append(newt)
tmp = sorted(tmp, reverse=True)
#print(tmp)

print('The top 5 most common words are:')
for v,k in tmp[:5]:
    print(k,v)
