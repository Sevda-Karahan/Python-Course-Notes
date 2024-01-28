print("\n***Exercise 5 - Part 1***")
print("***Functions***")
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

print("\n***Exercise 5 - Part 2***")
big = max("Hello world!")
print(big)
tiny = min("Hello world!")
print(tiny)

#################################################################

print("\n***Exercise 6 - Part 1***")
def greet(lang):
    if lang == 'tr':
        print("Merhaba!")
    elif lang == 'es':
        print("Hola!")
    elif lang == 'fr':
        print("Bonjour!")
    else:
        print("Hello!")

greet('tr')
greet('en')
greet('fr')
greet('es')
greet('random')

def greet():
    return "Hello"

print(greet(), "Sevda")


def greet(lang):
    if lang == 'tr':
        return "Merhaba"
    elif lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print(greet('tr'), "Sevda")
print(greet('en'), "Sevda")
print(greet('es'), "Sevda")
print(greet('fr'), "Sevda")

#################################################################

print("\n***Exercise 6 - Part 2***")
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

#################################################################

print("\n***Exercise 7 - Part 1***")
def computepay(hours, rate):
    pay = float(hours) * float(rate)
    if int(hours)>40 :
        pay += 0.5 * (float(hours) - 40) * float(rate)
    return pay


hours = input("Enter hours: ")
rate = input("Enter rate: ")
pay = computepay(hours, rate)
print("Pay:", pay)
