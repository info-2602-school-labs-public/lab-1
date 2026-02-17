# Lab 1

##==================================================

## Python Syntax 1

##--------------------------------------------

### Variables Assignment & Operators

#### Comments in python begin with a single hashtag

x = 10 # -> Variables are declared and initialized without type keywords
print(x) # -> A variable can be printed out using the print function

x = 23 # -> Variables can be reassigned
print(x)

y = None # -> Variables can be declared but not assigned to a value by using the keyword "None" (null doesn't exist in python)
print(y)

y = 2

z = (x + y)/x + (78%3) # -> usual mathematical operations supported
print(z)

#### -> Note: Variable names cannot begin with numbers, clash with keywords, or include dashed or spaces.

##--------------------------------------------

### Primitive Types and Strings

name = "bobby"
nameType = type(name) # -> The type() function returns the type of a variable
print(nameType) # -> This should indicate that the variable is a string (<class 'str'>)

age = 12
ageType = type(age)
print(ageType) # -> This should indicate that the variable is an integer (<class 'int'>)

height = 6.5
heightType = type(height)
print(heightType) # -> <class 'float'>

hasDate = False
hasDateType = type(hasDate)
print(hasDateType) # -> <class 'bool'>

comp = 7j
compType = type(comp)
print(compType) # -> <class 'complex'>

#### Using fstrings for interpolation

message = f'Hi my name is {name} I am {age} years old'
print(message) # -> 'Hi my name is bobby I am 12 years old'

#### type casting to convert thypes
intHeight = int(height) # -> converts float to int: 6
strHeight = str(height) # -> converts float to string: '6'
floatHeight = float(intHeight) # -> converts int to float: 6.0

##--------------------------------------------

### Input Output

name = input("Enter name: ") # -> reads input
print (name) # -> prints output

#### -> Note: The most important thing you should know about python is its indentation syntax. It does not use "{}" for scope. Scope is explicitly delimited with indentation

##--------------------------------------------

### Comparison

#### -> Note: if statements do not use parentheses () or squiggly braces {} instead it uses a colon : and indentation is used to delimit the condition and scope

#### correct

if 3 > 5:
    print("more") # -> The body of the if statement is this single line
else :
    print("less") # -> The body of the else statement is this single line

#### Single line if-else statements can be written like this
#### However this makes the code unreadable and is discourages

if 3 > 5: print("more")
else: print("less")

#### "else if" in python is written as "elif"
mark = input("Enter mark: ")
mark = int(mark)
if mark > 70:
    print("A")
elif mark > 60: # -> Note the use of "elif"
    print("B")
elif mark > 50: # -> Note the use of "elif"
    print("C") 
else:
    print("F")

##--------------------------------------------  

### Iteration

i = 1
while i < 10:
    print(i)
    i += 1 # -> shorthand for i = i + 1
else:
    print("This is run when the loop condition is no longer met")

#### iterating an iterale such as a list
list = ["bob", "sally", "john"]
for j in list:
    print(j)   

#### iterating between custom range and increment
for i in range(0, 10, 2): # -> range(start, end, step)
    print(i)

#### -> Note: For incrementing variables, python does not support i++, instead it uses i+=<value>
#### -> Note: For iteratig elements in a list in python, we use for..in, but in Javascrit we use for..og. Keep this difference in mind as for...in is valid syntax in Javascript but does something completely diffrent than for..of

##--------------------------------------------

### Functions

#### basic functions
def add(a, b): # -> functions are declared using the def keyword
    return a + b # -> return keyword is used to return values from functions    

def printPerson(name, age, height):
    print(name, age, height)

#### you can specify arguments in any order if they are named 
printPerson(age=12, name='bob', height=5)

#### default arguments are ued when they are not given in the function call
def sayHello(fname, lname='Smith'):
    print('Hello '+fname + ' ' + lname)

sayHello('John') # -> uses default argument for lname
sayHello('Bill', 'Young') # -> uses given argument for lname

#### functions can return multiple values
def multiReturnFunc(a,b): 
    return a+b, a-b, a*b, a/b

#### you can assign multople variables to the values being returned by the function
numSum, numDiff, numMult, numDiv = multiReturnFunc(10, 5)
print(numSum, numDiff, numMult, numDiv)

##--------------------------------------------

##==================================================

## Python Syntax 2

##--------------------------------------------

### Lists

#### -> Note: Lists are your arrays in python, they can include elements of different data types.

list = ['item1', 'item2', 'item3'] # -> lists are declared using square brackets []
list2 = [12, 33, 45, 58, 23]

print(list)

#### negative indexing can access elemements starting from the end
print(list2[-1]) # -> prints 23

#### select a subset of a list
print(list2[2:4]) # -> prints [45, 58] (inclusive of start index, exclusive of end index)

#### gets the length of a list
print(len(list2)) # -> prints 5

#### add items to list
list.append('item4') # -> adds item to end of list

#### remove items from list
item4 = list.pop() # -> removes and returns last item from list

#### copy list
list3 = list2.copy() # -> creates a copy of list2

#### list comprehension, lets you create new ists from existing lists
num = [1, 2, 3, 4]
doubled = [n*2 for n in num] # -> creates a new list with each element doubled
print(doubled) # -> prints [2, 4, 6, 8]
odd = [n for n in num if n%2 != 0] # -> creates a new list with only odd elements
print(odd) # -> prints [1, 3]

#### unpacking a list, lets you create variables from items in the list
num = [1, 2, 3, 4]
[first, second, *rest] = num # -> unpacks first two elements into variables, and the rest into a list
print(first) # -> prints 1
print(second) # -> prints 2
print(rest) # -> prints [3, 4]

#### joining lists
num2 =[5, 6]
num3 = num + num2 # -> joins two lists into a new list
print(num3) # -> prints [1, 2, 3, 4, 5, 6]

#### copying lists
num4 = num2.copy() # -> creates a copy of num2

##--------------------------------------------

### Tuples

#### -> Note: Tuples are collections that are ordered and unchangeable, because of this they faster than lists. 
#### -> Note: Tuples are similar to lists but they are immutable (cannot be changed after creation)

thistuple = ("apple", "banana", "cherry", "apple", "cherry") # -> tuples are declared using parentheses ()
print(thistuple); # -> ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple[0]); # -> 'apple'

##--------------------------------------------

### Sets

#### -> Note: Sets are collections that do not allow duplicates, they are useful for algorithms that ned to keep track of unique occurrences. 
#### -> Note: Sets are unordered collections of unique elements. They are useful for membership testing and eliminating duplicate entries.

data = [20, 3, 20, 42, 2, 3, 10, 32, 2]

myset = {0, 1}

for num in data:
    myset.add(num) # -> adds elements to the set

print(myset) # -> prints {0, 1, 2, 3, 10, 20, 32, 42}
num_unique = len(myset) # -> gets the number of unique elements in the set

#### -> Note: there's also a number of useful methods available on sets such as issubset(), intersecion(), and difference().
#### -> Note: Lists, Sets and Tuples are iterables and therefore suport the for x in collection syntax

##--------------------------------------------

### Dictionaries

#### -> Note: Dictionaries are the python equivalent of Javascript's object literals. They are simply key value pairs and work
#### -> Note: Dictionaries are used to store data values in key:value pairs. They are unordered, changeable, and do not allow duplicates.

mydict = {
    "name":"bon",
    "age": 34
}

print(mydict) # -> {'name': 'bon', 'age': 34}

#### assessing a key
print(mydict["age"]) # -> 34

#### adding a new key and value
mydict["height"] = 7

#### iterating keys
for key in mydict:
    print(key)

#### iterating values
for key in mydict:
    print(mydict[key])

#### check for a key
if 'weight' in mydict:
    print(mydict['weight'])
else:
    print('no weight property!')

##--------------------------------------------

### Classes
#### -> Note: Classes are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.

#### Parent class
class Person:
    def __init__(self, name, height, weight): # -> constructor method
        self.name = name; 
        self.height = height; 
        self.weight = weight; 

    def sayHello(self):
        print("Hello! I'm a person, my name is", self.name)

#### Child class inherits from Person
class Student(Person):

    # -> super is the refernece to the parent class Person, so we call Person's constructor here to se the Person properties of the student instance
    def __init__(self, stid, name, height, weight):
        super().__init__(name, height, weight) 
        self.stid = stid;   

    # -> override method of parent
    def sayHello(self):
        print("Hello! I'm a student, my name is", self.name)

bob = Person('bob', 12, 34)
sally = Student(123, 'sally', 7, 34)

bob.sayHello() # -> Hello! I'm a person, my name is bob
sally.sayHello() # -> Hello! I'm a student, my name is sally

print(bob.name) # -> bob