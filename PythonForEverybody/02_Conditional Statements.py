print("\n***Exercise 3 - Part 1***")
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

################################################################

print("\n***Exercise 3 - Part 2***")
astr = 'Bob'
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1
print("Done", istr)

################################################################

print("\n***Exercise 3 - Part 3***")
rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print("Nice work")
else:
    print("Not a number")

################################################################

print("\n***Exercise 4 - Part 1***")
hours = input("Enter hours: ")
rate = input("Enter rate: ")
pay = float(hours) * float(rate)
if int(hours)>40 :
    pay += 0.5 * (float(hours) - 40) * float(rate)
print("Pay:", pay)

################################################################

print("\n***Exercise 4 - Part 2***")
flag = 1
while flag == 1:
    flag = 0
    hours = input("Enter hours: ")
    rate = input("Enter rate: ")
    try:
        pay = float(hours) * float(rate)
    except:
        print("Error, please enter numeric input")
        flag = 1
print("Pay:", pay)
