#This is a Python test

x = 1

print("Hello World")

print(f"I just wanted to say {x} is cool")

if x == 1:
    print(f"{x} is the first number")

print("myint = (Whole number here) will print out a whole number")
myint = 1
print(myint)

print("Here is 1 in a decimal")

myfloat = 1.0
print(myfloat)
print("You can use myfloat = float(Integer here) to turn a whole number into a decimal")
myfloat = float(1)
print(myfloat)

print("mystring = 'Words here' are defined with either a single quote or double quotes")
mystring = '1 is my favorite number to exist'
print(mystring)

print("I have \"one = 1\" and \"two = 2\" and \"three = one + two\". To explain it, \"three = one + two\" will add \"one\" and \"two\" together and you get the result below")
one = 1
two = 2
three = one + two
print(three)

print("But let's use words now! We have \"Number = 'Number'\" and \"One = 'One'\". We will use \"NumberOne = Number + " " + One\", which will combine both words")
number = 'Number'
one = 'one'
numberone = number + " " + one
print(numberone)

print("We can assign multiple variables simultaneously with for example \"a, b = 3, 4\" followed by \"print(a, b)\".")
a, b = 3, 4
print(a, b)

print("Note that mixing operators between numbers (one = 1 for example) and strings (one = 'One' for example) is not supported.")

#All about Lists!

print("Here is a list of the first 5 numbers!")

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print(mylist[3]) # prints 4
print(mylist[4]) # prints 5
#prints out 1,2,3
for x in mylist:
    print(x)

print("Now let's get into math!")
number = 1 + 2 * 3 / 4.0
print(number)
print("Solving this problem was possible thanks to \"number = 1 + 2 * 3 / 4.0\".")
print("let's do a remainder problem, which is done with \"remainder = number % number\".")
remainder = 11 % 3
print(remainder)

print("A new story about a man who is on a programming adventure")
name = "Peter"
age = "12"
print(f"Hello, my name is {name} and I'm {age} years old")

mylist = [3, 5, 7]
print(f"A list of numbers I need to find: {mylist}")

astring = "Hello 3"
astring2 = "Hello Peter"

print("single quotes are ' '")

print(len(astring))\

print(astring.index("3"))
print(astring.count("l"))

print(astring[3:7])
print(astring[::-1])

print(astring.upper())
print (astring.lower())

# Left off on Conditions section on learnpython.org

print("Let's go over conditions! Let's start with numbers! We have E = 5 here, so let's see what the bottom outputs")
e = 5
print(e == 5) # Outputs true
print(e == 3) # Outputs false
print(e < 3) # Outputs false

if name == "Peter" and age == "12":\
    print("Your name is Peter and your age is 12")

if name == "Peter" or name == "John":
    print("Your name is either Peter or John")

if name in ["Peter", "John"]:
    print("Your name is either Peter or John")

statement = True
another_statement = False
if statement is True:
    print("That is correct")
else:
    print("That is incorrect")

t = 10
if t == 10:
    print("t equals ten!")
else:
    print("t does not equal ten")

# This is an operator

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# Left off on Loops on learnpython.org

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

print("This is an example of looping that shows numbers from 0-5")
for x in range(6):
    print(x)

print("This is another example that shows the numbers between 1-6")
for x in range(2, 6):
    print(x)

print("Prints out 3,5,7")
for x in range(3, 8, 2):
    print(x)

print("This is for the \"While\"loops operation.")
count = 0
while count < 5:
    print(count)
    count +=1 # This is the same as count = count + 1

print("This is about the \"break\" and \"continue\" operations.")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("This for the continue statements")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
    
print("This is for the \"Else\" command in loops.")
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if(1%5==0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition.")

# Left off on functions on learnpython.org