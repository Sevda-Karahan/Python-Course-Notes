######################################################################################################################
str1 = "Hello "
str2= "there!"

bob = str1 + str2
print(bob)

str3 = "123"
print(str3)
str3 = int(str3) + 1
print(str3)

######################################################################################################################

# Reading and converting
name = input("Enter name: ")
print(name)

str = input("Enter number: ")
x = int(str) - 10
print(x)

######################################################################################################################

#Looking inside strrings
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

######################################################################################################################

zot = 'abc'
print(zot[2])

######################################################################################################################

fruit = 'banana'
print(len(fruit))

######################################################################################################################

# Looping trough strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

######################################################################################################################

# Looping trough strings
fruit = 'banana'
for letter in fruit:
    print(letter)
print("******************")
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

######################################################################################################################

# Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

######################################################################################################################

# Slicing strings
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:11]) #Pytho
print(s[6:12]) #Python
print(s[6:20]) #Python

# string[a:b] means -> start from a, go up to b (a included, b not included)

print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python
