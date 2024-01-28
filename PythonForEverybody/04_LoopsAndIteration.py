#INDEFINITE LOOPS
##################################################################################################

# Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print("DONE!")

##################################################################################################

# Finishing an iteration with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("DONE!")

#DEFINITE LOOPS
##################################################################################################

for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")


##################################################################################################

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year', friend)
print('Done!')

#LOOPS AND ITERATION EXERCISES
##################################################################################################

# Finding the largest value
largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print("Largest so far", largest_so_far)
print("After", largest_so_far)

##################################################################################################

# Counting in a loop
# Summing in a loop

# Finding the average in a loop
count = 0
sum = 0
print("Before: count ", count, ", sum ", sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum += value
    print("count ", count, ", sum ", sum, ", value ", value)
print("After: count ", count, ", sum ", sum, ", Average ", (sum/count))

##################################################################################################

#Filtering in a loop
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20 :
        print("Large number", value)

##################################################################################################

# Search using a boolean variable
found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

##################################################################################################

# Find the smallest value
list = [9, 41, 12, 3, 74, 15]
smallest_so_far = list[0]
print("Before", smallest_so_far)
for value in list:
    if value < smallest_so_far:
        smallest_so_far = value
    print(smallest_so_far, value)
print("After", smallest_so_far)

##################################################################################################

# Find the smallest value - (2. aproach)
smallest = None
print("Before", smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest == None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

##################################################################################################

total = 0
count = 0
while str != "done":
    str = input("Enter a number: ")
    try:
        istr = int(str)
        count += 1
        total += istr
    except:
        if str != "done":
            print("Invalid input")
try:
    print(total, count, (total / count)) # (total / count) can cause divison by zero error
except:
    print("")
