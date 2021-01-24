# PYTHON FOR ABSOLUTE BEGINNER

# Assigning value to a variable

# assigned 5 initially
ex_var = 5
# reassigned a different value to the same variable and so the value of the variable is changed
ex_var = 7

# Variables and assignment test
a = 1       # holds integer value
b = 1.25    # holds float value
c = True    # holds string value
# value is reassigned to variable a
a = 2

# COMMENTS AND MATH OPERATORS
# Math Operator - Basic math operator
addition = 4 + 5
subtraction = 5 - 2
division = 7 / 2
multiplication = 3 * 8

# Exponentiation, Floor division and Modulo
exponentiation = 4 ** 4
Floor_division = 16 // 5
Modulo = 7 / 3

# Performing mathematical operations in different ways
add_assign = 5
add_assign += 7
# The above expression can also be written as
add1 = 5
add1 = add1 + 7
# Similarly subtracttion, multiplication, division, exponentiation, floor division and modulo
sub = 10
sub -= 5    # 5
mul = 5
mul *= 5    # 25
div = 10
div /= 5    # 2
exp = 10
exp **= 2   # 100
fd = 10
fd //= 6    # 1
mod = 10
mod %= 7    # 3

# print() FUNCTION
value = 3.14
value_1 = True
value_2 = 150

print(value)
print(value_1)
print(value_2)

# it is possible to print the variable values directly
print(2020)
# To print string
print(' Hello ')

# print can be used for displaying the result of the expression
value_3 = 10 + 2
print(value_3)
print((3+2)*2)

# print() exercise solutions
# Exercise 1
var_1 = 2020
print(var_1)    # display 2020 as output

# Exercise 2
print(3.14)     # displays the float value as output

# Exercise 3
print((5+3)*2)  # the answer 16 will be displayed as output

# FLOAT POINT ERRORS
print(1.23 + 2.80)  # gives 4.02 as output, and this answer is wrong

# To overcome the above error 2 methods are used in python
# 1. float to integer conversion calculation
value_4 = (123 + 280)/100   # Correct answer 4.03 will be printed

# 2. Use of round() funstion
print(round(value_4, 2))    # Correct answer 4.03 will be printed

# Grocery Purchase solution
Penne = 16.68 * 100
Pasta = 6.98 * 100
Garlic = 16.78 * 100
Italian_seasoning = 15.26 * 100
Baguettes = 3.00 * 100
Meatballs = 4.39 * 100
subtotal = Penne + Pasta + Garlic + Italian_seasoning + Baguettes + Meatballs

print(subtotal)     # 6309 is the output

Total = subtotal / 100
print(Total)    # actual answer 63.09

# round function answer
subtotal_1 = round((Penne + Pasta + Garlic + Italian_seasoning + Baguettes + Meatballs), 2)
# or we can also do "print(round(subtotal, 2))"
# the above code helps to give the actual answer for the grocery purchase program

# STRING PART 1
str1 = 'This is a string'
str2 = "This also a string"
str3 = '1984!'
str4 = "LiVe LONG and PRosPer."
str5 = "!@#$%^&*()_-=++/.,';][{}:|><?"
str6 = ""

# use of index value in string
str7 = "Sayeesudha"
print(str7[2])  # prints y
print("Sudha"[3])   # prints h

# Slicing of a string
str8 = "Sayeesudha_Senthil_Velan"
print(str8[:10])    # prints Sayeesudha
print(str8[11:18])  # prints Senthil
print(str8[19:])    # prints Velan

# String Concatenation

print("Sayee" + " " + "Sudha")  # prints Sayee Sudha
print("Sayee" +"sudha")         # prints Sayeesudha
str9 = "Sayeesudha" + "_" + "Senthil" + "_" + "Velan"
print(str9[0],str9[11],str9[19])    # prints S S V
print(str9[11:18])  # prints Senthil
print(str9[11:])    # prints "Senthil_Velan
print(str9[0:18])   # prints "Sayeesudha_Senthil"

# STRING EXERCISES SOLUTIONS

ex_1 = "Just do it!"
print(ex_1[10])     # prints !
print(ex_1[5:7])    # prints do
print(ex_1[8:])     # prints it!
print(ex_1[:4])     # prints Just

# one way to perform concatenation
ex_2 = ex_1[5:]
ex_3 = "Don't"
print(ex_3 + " " + ex_2)    # prints Don't do it!

# Another method of concatenation
print("Don't" + " " + ex_1[5:])     # prints Don't do it!

# type function
x = True
y = 3.14
z = 24

print(type(x))      # output is boolean
print(type(y))      # output is float
print(type(z))      # output is integer

# string function "str()"

x1 = str(True)
y1 = str(3.14)
z1 = str(24)
print(type(x1))     # output for all the three will be string
print(type(y1))
print(type(z1))

# ESCAPE SEQUENCE
# use of tab, new line and \' and \"
print('"Hello \'Steve\'",\n\t how is it going for you on your \"Search\"')
print("\'Thanks for asking\'\n\n")

# PRACTICE EXERCISE FOR type(), str(), escape sequence
a = 3.11
print(type(a))  # float data type
print(str(a) + " is a float")   # converts 'a' to string and add teh statement 'is a float'
print('\"Hello, I\'m Sayee, it\'s nice to meet you!\"')

# code for asterisk triangle

print('\t\t*******')
print('\t\t *****')
print('\t\t  ***')
print('\t\t   *')

print('*******\n *****\n  ***\n   * ')

# input() FUNCTION
# using raw_input() function ask the name of the user

name = raw_input("Please enter your name:")
print("Your name is" + name + ".")
print(type(name))

# input function will accept input from user and will assign those inputs as string data type
fav = raw_input("Please is your favourite number?")
print("Your favourite number is" + fav + ".")
print(type(fav))

# Monty Challenge
nam = raw_input("What is your name?")
quest = raw_input("What is your quest?")
fav_color = raw_input("What is your favourite color?")
print("So your name is" + nam + ",your quest is" + quest + ", and your favorite color is" + fav_color)

# int() function

user_int = int(raw_input("Please enter an integer:"))
print(user_int)
print(type(user_int))

# float() function

user_float = float(raw_input("Please enter an float:"))
print(user_float)
print(type(user_float))

# int() exercise
user_value = int(raw_input("Please enter an integer:"))
print(user_value + 10)

# Function with single parameter
def addition(val_1):
    print(val_1 + 2)


addition(8)

# multiple parameters used in an function
First = "The number "


def print_statement(p1, p2, p3):
    print(p1 + str(p2) + p3)


print_statement(First, 5, " is an integer")


# Default parameter
# by default we are providing the values which is needed to calculated by the program
def mul(x=5, y=3):
    print(x * y)


mul(10, 3)


# return keyword use in function
# to used the output of a function with another function, return keyword is used
def multi(a=5, b=6):  # default values 5 and 6 will be passed in the function
    return a * b  # default values calculation - 30


print(multi() + 30)  # the result of previous step (30) is added again with 30 = 60
result = multi(2)  # here the default value of a is changed by the argument passing 2
# so the result of the return function would be 2*6 = 12
print(result)  # 12 is printed


# Function with no parameter exercise
def hello_world_printer():
    print("Hello World")


hello_world_printer()


# Function with 1 parameter exercise
def name_printer(given_name):
    print(given_name)


name = raw_input("Please enter your name:")
name_printer(name)

# Programming challenge: Volume of a rectangular prism
length = int(raw_input("Enter the length of the Prism"))
width = int(raw_input("Enter the width of the Prism"))
height = int(raw_input("Enter the height of the Prism"))


def volume_prism(l, b, h):
    return l * b * h


result = volume_prism(length, width, height)
print("The volume of the rectangular prism is:" + str(result))

# Programming Challenge: Celsius to Fahrenheit
Celsius = int(raw_input("Enter the Celsius value:"))


def Fahrenheit(user_value):
    return (18 * user_value + 3200)/10


result = Fahrenheit(Celsius)
print("The Fahrenheit equivalent of " + str(Celsius) + " degrees Celsius is: " + str(result))


def Fahrenheit_1(user_value):
    val = 1.8 * user_value + 320
    return round(val, 1)


result = Fahrenheit_1(Celsius)
print("The Fahrenheit equivalent of " + str(Celsius) + " degrees Celsius is: " + str(result))

# To import a module we use 'import' keyword
# random module is imported to randomly pick some value between the range of 1 to 10

# import random
# print(random.randint(1, 10))

# To import a function from a module

# from random import randint
# print(randint(10, 20))

# To import every function form a module without the need to define them in future code
# random() function is used to call random  float values by default from the range of 0.0 to 1.0
from random import *
print(random())

# Programming Challenge: Miles per Gallon

from random import randint

gallons = randint(10, 25)
miles = randint(200, 400)

print("The car can travel " + str(miles // gallons) + " miles per gallons")
print("The car's fuel tank can hold: " + str(gallons) + " gallons")
print("The car can travel " + str(miles) + " miles for a full tank")

# def MPG(gal, mile):

#    return mile//gal


# Gallons_used = MPG(gallons, miles)

# print("Gallons of gas used by the car: " + str(gallons))
# print("The car travelled this much miles " + str(miles) + " for this much gallons " + str(gallons))
# print("The approximate number of miles per gallon is: " + str(Gallons_used))

# Variable Scope
# You can have the same name for different variables
# as long as they are in different scope

def first():
    global fruit    # the "Apple" is the global value for the variable fruit
    fruit = "Apple"  # local variable 1
    print(fruit)


def second():
    fruit = "Banana"    # local variable 2
    print(fruit)


fruit = "Papaya"        # global variable value is changed to "Apple"
first()
second()
print(fruit)

# Flow control conditional operators
print("\n" + str(4 > 2))
print(8 < 3)
print(5.25 < 6)
print(5 <= 5)
print(9 >= 2)
print(9 != 9)
print(9 != 10)
print(9 == 9)
print(9 == 10)
print("Hello" != "hello")
print("hello" == "World")

# Boolean Operators
# AND operator
print('\n')
print("Hello" == "Hello" and "hi" != "Hello")
# OR Operator
print(3.4 <= 4 or 4 >= 5)
# NOT Operator
print(not 4.5 > 6)
print(not "Python" != "Python")
# Flow control statements
# if statement

num = raw_input("\nEnter a number between 1 to 10: ")


if int(num) <= 10:
    print("The number you have entered is: " + num)


veg = raw_input("\nName a vegetable: ")

if veg == "corn":
    print("The vegetable you have entered is: " + veg)

# Else statement

num = raw_input("\nEnter a number between 1 to 10: ")


if int(num) <= 10:
    print("The number you have entered is: " + num)
else:
    print("The given number " + num + " is out of the specified range")


veg = raw_input("\nName a vegetable: ")

if veg == "corn":
    print("The vegetable you have entered is: " + veg)
else:
    print("The vegetable you have entered is not corn")
# if else statement

gpa = float(raw_input("Enter your gpa: "))
institute = raw_input("Is the institute specified is valid for loan: Y/N? ")
if gpa >= 3.7:
    if institute == "Y" or institute == "y":
        print("The applicant is qualified for a loan")
    else:
        print("REJECTED: The candidate's institute is not valid for a loan process")
else:
    print("REJECTED: The candidate has less GPA value")

# Programming Challenge: Grade determiner

score = int(raw_input("\nEnter the student's score:"))

if score >= 90:
    print("\nFor the score " + str(score) + " the student gets A Grade")
else:
    if score >= 80:
        print("\nFor the score " + str(score) + " the student gets B Grade")
    else:
        if score >= 70:
            print("\nFor the score " + str(score) + " the student gets C Grade")
        else:
            if score >= 60:
                print("\nFor the score " + str(score) + " the student gets D Grade")
            else:
                if score < 60:
                    print("\nFor the score " + str(score) + " the student gets F Grade")

# elif statement
user_num = int(raw_input("\nPlease enter a number:"))
if user_num < 0:
    print("The user has entered a number less than 0")
elif user_num == 0:
    print("The user has entered the value 0")
elif 0 < user_num <= 100:
    print("The user has given a number between the range of 1 to 100")
else:
    print(" The use has entered a value which is greater than 100")

# Programming Challenge: Roman Numeral Equivalent
from random import randint

var = randint(1, 10)
if var == 1:
    print("\n For the integer " + str(var) + "the roman value is - I")
elif var == 2:
    print("\n For the integer " + str(var) + "the roman value is - II")
elif var == 3:
    print("\n For the integer " + str(var) + "the roman value is - III")
elif var == 4:
    print("\n For the integer " + str(var) + "the roman value is - IV")
elif var == 5:
    print("\n For the integer " + str(var) + "the roman value is - V")
elif var == 6:
    print("\n For the integer " + str(var) + "the roman value is - VI")
elif var == 7:
    print("\n For the integer " + str(var) + "the roman value is - VII")
elif var == 8:
    print("\n For the integer " + str(var) + "the roman value is - VIII")
elif var == 9:
    print("\n For the integer " + str(var) + "the roman value is - IX")
elif var == 10:
    print("\n For the integer " + str(var) + "the roman value is - X")
else:
    print("The given integer " + str(var) + " is out of rage")

# Truth and False values
str_1 = raw_input("Enter some statement: ")
if str_1:
    print("Thanks for entering something")
else:
    print("You did not enter anything")

print("\n")
print(bool(0.0))

# While  Loop
counter = 10     # assigning the iteration value

while counter != 0:
    print("\n")
    print(str(counter))
    counter -= 1

# Programming Challenge: Sum of Numbers From a Positive Integer
value_0 = int(raw_input("\nEnter a positive integer values: "))
value_1 = value_0
summed = 0

while value_1 >= 1:
    summed = summed + value_1
    value_1 = value_1 - 1

print("The given number by the user is: " + str(value_0))
print("The sum of all the integers of the given number is: " + str(summed))

# For loop
# If strings are initialized as values in for loop then,
# Based on the number of letters available in he string,
# Each letter of the string will be printed as output in every new line
word = "house"

for letter in word:
    print(letter)

word_1 = "Hello World"

for letter_1 in word_1:
    print("\n" + letter_1)

# Programming Challenge: Find the number of Characters in a string

num_char = raw_input("\nEnter a string: ")
sum_value = 0

for char_count in num_char:
    sum_value = sum_value + 1

print("The string entered by the user: " + num_char)
print("The umber of characters in the string:" + str(sum_value))

# range()
# range() used for one argument
# It starts the loop from 0 and ends with the number count 1 less than the given range

data_0 = range(5)

for num in data_0:
    print("\n" + str(num))

print(type(data_0))

# range() used for 2 arguments
# the first argument says the starting position value of initialization
# the second argument says the range length and it is 1 less the given range
data_1 = range(5, 10)

for num in data_1:
    print("\n" + str(num))

# range() used for 3 arguments
# 1st argument - start position of initialization
# 2nd argument - the length of the range and it is 1 less than the specified range
# 3rd argument - step of range value which is to be expanded // it can be a (-) range
data_2 = range(1, 20, 3)

for num in data_2:
    print("\n" + str(num))

# range specified in reverse order
data_3 = range(20, 1, -3)

for num in data_3:
    print("\n" + str(num))

# Programming Challenge:
for num_value in range(1, 51):
    if num_value % 3 == 0 and num_value % 5 == 0:
        print("FrizzBuzz")
    elif num_value % 3 == 0:
        print("Fizz")
    elif num_value % 5 == 0:
        print("Buzz")
    else:
        print(num_value)

# Programming Challenge: Factorial


def factorial(val):

    cal = 1
    for val_1 in range(val, 1, -1):
        cal = val_1 * cal

    return cal


print(factorial(3))
print(factorial(4))
print(factorial(5))

# String Methods
# To change the case to upper or lower

all_low = "this is an important try out exercise"
print(all_low.upper())  # Though upper() was called
print(all_low)          # the actual value of all_low is not changed
all_up = "HELLO!"
print(all_up.lower())   # Similar to upper(); lower() also does the same
print(all_up)

# isupper() and islower()
print("HELLO".isupper())
print("Hello".isupper())
print("hello".islower())
print("Hello".islower())

# multiple string function can be defined in a single statement
print("\nHELLO".lower().isupper())

# isalpha function
print("Batman".isalpha())
print("Batman123".isalpha())

# isalnum function
print("Batman123".isalnum())
print("Batman".isalnum())
print("123".isalnum())

# isdecimal function in python2.7 it isdigit()
print("123".isdigit())
print("3.14".isdigit())

# isspace function
print(" ".isspace())
print("       ".isspace())
print("Hello World".isspace())

# on considering specific location of the statement where space is involved
# Then isspace will return TRUE
print("Hello World"[5].isspace())

# istitle function
print("The King Strikes Back".istitle())
print("The King Strikes Back!!".istitle())
print("The king strikes back".istitle())
# title method changes the normal string to title case
print("The king strikes back".title().istitle())

# startswith()
print("The king goes beyond everyone's expectations!".startswith("The"))
print("The king goes beyond everyone's expectations!".startswith("T"))
print("The king goes beyond everyone's expectations!".startswith("t"))
# endswith()
print("The king goes beyond everyone's expectations!".endswith("expectations!"))
print("The king goes beyond everyone's expectations!".endswith("expectations"))
print("The king goes beyond everyone's expectations!".endswith("!"))

# join() is used for combining two different strings
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))

# split() is used to split the string sentence
print("Egg, Waffles, Butter, Cheese, Milk".split())
print("Egg, Waffles, Butter, Cheese, Milk".split(','))
print("Egg, Waffles, Butter, Cheese, Milk".split(', '))

# String Method exercise

mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith('A'))
print(mixed_case.endswith('e'))
words = mixed_case.split()
print(words)
print("".join(words).isalpha())

# rjust and ljust
# both can take more than one argument to do right and left justify
print("Hello  world".rjust(15))     # 11 in length so it it gives four spaces in front
print("Hello  world".ljust(15) + "four spaces")

# rjust and ljust - use of 2nd argument
# This argument should be a string
print("Hello  world".rjust(15, '_'))
print("Hello  world".ljust(15, '*') + "four spaces")

# center() - it can take two argument
print("Hello  world".center(15))
print("Hello  world".center(15, ':'))

# strip, rstrip and lstrip functions
# are useful when you want to remove characters such as white spaces from a string
# a specific character can also removed using these functions
# arguments for these method must be a string
print("I had an exciting trip!!!111111")
print("I had an exciting trip!!!111111".strip("1"))
print("I had an exciting trip!!!111111".lstrip("1"))
print("I had an exciting trip!!!111111".rstrip("1"))

# strip multiple characters
print("juice, bread, cream, Milk, bread".rstrip(", bread"))
# though the bread term is rearranged, still bread will be removed
print("juice, bread, cream, Milk, bread".rstrip(",ad bre"))
print("blueblueyellowblue".strip("blue"))
print("blueblueyellowblue".strip("eulb"))

# replace function
print("Good morning".replace("morning", "Afternoon"))

# Strip method 2 Exercises
the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))

# len() function
# It counts the number of characters in the string

print(len("Sayee"))
print(len("Sayeesudha!!"))

# len() used in strings which uses concatenation or slicing concept
print("This" + " " + "is" + " " + "a" + " " + "string.")
print(len("This" + " " + "is" + " " + "a" + " " + "string."))
print("SayeesudhaSenthilvelanisverytalented"[10:22])
print(len("SayeesudhaSenthilvelanisverytalented"[10:22]))

# Programming Challenge: Reverse a string

user_input = raw_input("Enter a string:")
data_0 = ""

for reverse in range(len(user_input) - 1, -1, -1):
    data_0 = data_0 + user_input[reverse]

print(data_0)

# Check whether the given string is palindrome or not
user_input = raw_input("Enter a string: ")
data_0 = ""
data_1 = user_input

for reverse in range(len(data_1) - 1, -1, -1):
    data_0 = data_0 + data_1[reverse]

if data_0 == user_input:
    print("The given string is a Palindrome")
else:
    print("The given string not a Palindrome")

print(data_0)

# Programming Challenge - Word Counter
user_string = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it James Bond 007."
spaces_and_letters = ""
for char in user_string:
    if char.isalnum() or char.isspace() or char == "-" :
        spaces_and_letters += char
words = spaces_and_letters.split()
number_of_words = len(words)

print(words)
print(number_of_words)

# format() function

name = raw_input("\nPlease enter your name: ")
degree = raw_input("Please enter your education qualification: ")
job = raw_input("What is your current job? ")
experiences = raw_input("How many years of experience do you have? ")

print("{} majored in {}, works as a  {}, and has {} years of experience.".format(name, degree, job, experiences))

# list function
# A list variable can hold any data type
ex_list_1 = [5, 4, 2, 1]    # int
ex_list_2 = [2.18, 3.46, 5.9]   # float
ex_list_3 = ["Hello", "Hi", "Greetings", "Adios"]   # string
ex_list_4 = [True, False, True, True, False]    # Boolean
ex_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]   # list within list

# A list can contain different data types
ex_list_6 = [10, 3.14, "Happy", True, [1, 2, 3]]

# A list() function takes a iterative data type such as string
# as it's argument and convert to a list and then returns
print(list('blah'))

# in and not in operator
# Used to check whether the given data is there in the list or not
check_list = [1, 2, 3, 4]
print(1 in check_list)
print(8 in check_list)
print(8 not in check_list)
print(1 not in check_list)
# The above activity can also be assigned to a variable
# then provide correct output
eval_check_list = 8 not in check_list
print(eval_check_list)

# Exercises
list_1 = [2, 3.14, True, "Hello", [4, 5, 6]]
list_2 = list("Greetings")
print("\n")
print(list_2)
print('e' in list_2)
print('a' not in list_2)

# Accessing list data by using their index number
list_3 = ["Hi", "Hello", "Greetings", "Howdy"]
print("\n")
print(list_3[2])    # Greetings will be printed as output

# To access a string within another string
list_4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# variable name, list set which needs to accessed
# last value - index number of the data of that list
print(list_4[2][1])

# To get a character from the list of strings
list_3 = ["Hi", "Hello", "Greetings", "Howdy"]
print(list_3[2][0])

# Use of negative indexes
# It used to get the data from the list - last to first order
neg = [1, 2, 3, 4, 5, 6]
print("\n")
print(neg[-1])
print(neg[-2])
print(neg[-3])
print(neg[-4])
print(neg[-5])
print(neg[-6])

list_5 = [False, 365, 3.14, "Happy New Year"]
print("\n")
print(list_5[2] + 1.14)
print("I wish a very \"" + list_5[-1] + "\" - Sayee.")

# List slicing
# list slicing follows the same concept of string slicing
list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n")
print(list_6[:5])   # by default it starts with the first value of the list
print(list_6[4:8])
print(list_6[7:])   # by default it accesses till the last value of the list

# To add or remove values in the list
# Also to reassign a value in the list
# This can be done by using indexing and slicing method of list
list_7 = [2, 4, 6, 8, 10]
print("\n")
list_7[1] = 3   # it changes the value of 4 to 3
print(list_7)
list_7[1:4] = [3, 4, 5]     # it slices value of the list [4, 6, 8]
print(list_7)
# To add new values in the list
list_7[4:] = [9, 10, 11]
print(list_7)


# Exercises of indexes and slicing of list
items = [[0, 2], [4, 6], [8, 10], [12, 14]]
print("\nTo access the first list of the list")
print(items[0])
print("To access the first value of the first list")
print(items[0][0])
print("To access the value 14 from the list")
print(items[-1][-1])

items_1 = ["Chair", "Table", "Desk", "Lamp", "Bed"]
print("Access the string chair from the list by using neg indexes")
print(items_1[-5])
print("Most people own at least " + str(items[0][1]) + " " + items_1[0] + "s.")

items_2 = [0.98, 8.76, 6.54, 4.32]
print(items_2[1:])
print(items_2[1:3])
print(items_2[:2])

# del() method used in a list
planets = ["Pluto", "Mercury", "Venus", "Earth"]
del planets[0]  # this statement removes the word pluto from the list
print(planets)

# remove() function used in a list
planets = ["Pluto", "Mercury", "Venus", "Earth"]
planets.remove("Pluto")
print(planets)
# When repetitive data from the list is needed to be removed
colors = ["red", "orange", "blue", "red", "yellow", "red"]
colors.remove("red")    # only the first instances of the value "red" will be removed
print(colors)

# append() method
pets = ["dogs", "cats", "parrots"]
print(pets)
pets.append('fish')    # fish will be added at the end of the list
print(pets)

# insert() method
# you add the items anywhere in the list
pets = ["dogs", "cats", "parrots"]
# initially specify the index where the item needs to added
# then specify the item name
pets.insert(1, "turtle")
print(pets)

# sort() list
# To sort the numbers in a list
num = [2.59, 4, 100, 98, -3]
print(num)
num.sort()  # by default it sorts the list from least to higher values
print(num)
num.sort(reverse=True)  # performs descending function
print(num)

# To sort strings in the list in alphabetic order
strings = ["Sayee", "Anna", "Cheiw", "Karen", "Daniel"]
print(strings)
# it sorts the string by default from A to Z
strings.sort()
print(strings)
# To sort the strings from Z to A
strings.sort(reverse=True)
print(strings)

# sort of list which has mixed data types but not strings
mixed = [True, 4.25, -1, 0]
mixed.sort()
print(mixed)

# sort() of strings were done in ASCIIbettical order
# i.e, uppercase letters comes before lowercase letters
str_1 = ["Anna", "Karen", "Daniel", "beetroot", "apple", "mango"]
str_1.sort()
print(str_1)
str_1.sort(key = str.lower)
print(str_1)

# index method()
# it helps to know the index position of an item in a list
metals = ["Gold", "Silver", "Pearl", "Platinum", "Copper"]
# To know the index number of the item "Pearl"
print(metals.index("Pearl"))
# if an item is repeated multiple times in a list
# then it provide the index value of first position when it appeared
# in the list
num_values = [1, 3, 5, 0, 6, 8, 5, 10]
print(num_values.index(5))

# pop() method
bands = ["Queen", "The beatles", "Backstreet boys", "MUSE", "Linked park"]
end = bands.pop()   # this by default it removes the last item of the list
print(bands)
print(end)
# it is possible to remove a item from the list by using the index number
bands = ["Queen", "The beatles", "Backstreet boys", "MUSE", "Linked park"]
end = bands.pop(3)  # this removes MUSE from the list
print(bands)
print(end)

# del and list methods exercises
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(3, "snowy owl")
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())

# list are mutable
ex_1 = [1, 2, 3, 4]
# To change the value of 3 to 5
ex_1[2] = 5
print(ex_1)

# To change a character in a string is not possible
# as strings immutable, therefore we have to reassign the string to the variable again
ex_2 = "1234"
# ex_2[2] = 5 --> will throw an error as string s are immutable
# so reassign the string
ex_2 = "1254"
print(ex_2)

# it is ok to use the string from another string
# in order to form a new string
ex_3 = "No, you can't"
ex_4 = "Yes," + ex_3[3:11] + "!!."
print(ex_4)

# We can refer a assigned value
ex_5 = 3.14
ex_6 = "Coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7)
print(ex_8)

# This reference of reassigning cannot be done using list
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)
# Changes made in one variable will automatically
# reflect in another variable

import copy
ex_11 = [1, 2, 3, 4, 5]
ex_12 = copy.deepcopy(ex_11)
ex_12[2] = 4
print(ex_11)
print(ex_12)

ex_13 = ["bush",
         "fern",
         "tree",
         "moss"]
print(ex_13)

# In string to divide contents in lines
ex_14 = 2 + \
        4 + \
        1
print(ex_14)

# The line division in strings
ex_15 = "The Emp\
ire Strikes  \
back"
print(ex_15)

# Use of line continuation character for a concatenated string
ex_18 = "hello" + \
        "world"
print(ex_18)

# Dictionaries
# To create a dictionary - it should have a dictionary name
# then {key term: it's value}
# It is consist of key value pairs

consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}

# by using keys the values of the key is accessed
# to access a value from a dictionary
# name of the dictionary [key term which holds the value]
print(consoles["microsoft"])

# values from dictionaries can also be assigned to variables
val = consoles["microsoft"]
print(val)

# values from dictionaries can be used in expressions
print("The " + consoles["sony"] + " 4 is Sony's newest gaming console.")

# key = it can hold different data type
# and all these key terms can be used in the same dictionary
metal_hardness = {9: "corundum", 10: "diamond"}
floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}

# Dictionaries are unordered
# In python the list must in same order while comparison is involved
print([2, 4, 6] == [2, 4, 6])   # equivalent
print([2, 4, 6] == [6, 4, 2])   # not equivalent
# In contrast in dictionary
first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
print(first == second)  # it is equivalent as dictionaries are unordered

# Key error - if a key doesn't exist in the dictionary
# then this error will be thrown to user

# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# print(first[4])

# To check whether the key exist or not
# int and not in operators are used
# Boolean output is obtained
first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
print(0 in first)
print(4 in first)
print(1 not in first)
print(4 not in first)

# .key() method
# allows to collect all the keys from the dictionary
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_year.keys())

# You can also use a for loop with the Keys method
# to iterate through the keys of a dictionary.
for key in birth_year.keys():
    print(key)

# .values() is a method which allows to get all the values of the dictionary
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_year.values())
# You can also use a for loop with the values method
# to iterate through the values of a dictionary.
for value in birth_year.values():
    print(value)

# .items()
# To get all the values and keys of the dictionary at the same time
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_year.items())

# To iteratively display the items of the dictionary
# for loop can be used and
# it will have two place holder values key and value
for key, value in birth_year.items():
    # print(value)
    # print(key)
    print(key, value)


# To know the data type of keys, values and items()
print(type(birth_year.keys()))
print(type(birth_year.values()))
print(type(birth_year.items()))
print(list(birth_year.keys()))  # converts its data type to list
print(list(birth_year.values()))
print(list(birth_year.items()))

# to check if a value was in a dictionary
# instead of a key, in and not in operators of values() are used
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print("elizabeth" in birth_year.values())

# get() method
# this allows us to look for
# and to get a key from a dictionary and return something other than
# an error message which stops the program
# from continuing to run if the key is not found, you are probably
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
# To print something other than error message
# if else statement can be used
if 1975 in birth_year:
    print(birth_year[1975])
else:
    print("1975 is not a key in birth year")

# The statement can be simplified by using get() method
# Where the entire statement is written in one line
print(birth_year.get(1975, "1975 is not a key in birth year"))

# Since dictionaries are immutable
# variables assigned to a dictionary and
# the made in that variable will automatically reflect on the dictionary
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_year)
people = birth_year     # dictionary is assigned to the variable people
people[1982] = "madeline"   # changes are done in people variable
print(birth_year)   # changes will be reflected in the dictionary also

# If a dictionary is too long,
# we can also separate the items in the dictionaries in multiple lines
birth_year = {1994: "bill",
              1969: "emily",
              1982: "elizabeth",
              2000: "turner"}
# len() in dictionary
# is used to determine number of key and values that the dictionary contains
print(len(birth_year))

# Dictionary methods 2
# .fromkeys() method returns the dictionary using two values
# that it was given as arguments,
# the first argument it takes is used as keys
# this value must be a iterable values such as list or string
# each iterable value will be used as a key for the dictionary
# and the second argument is used as a value.
# it can be of any data type - int, float, bool, string, list, or another dict
ex_1 = {}.fromkeys(["address"], "Saint pauls terrace, QLD")
# Based on the above arguments
# fromkeys will generate a dic with one key value pair
print(ex_1)

# If string is passed as an 1st argument
ex_1 = {}.fromkeys("ad", "Saint pauls terrace, QLD")
# each character of the string will be passed as key in the dictionary
# and each key will hold the 2nd argument as value
print(ex_1)

# if same value is passed in during iteration
# then only one of that character will be considered
# as the key of the dictionary
ex_1 = {}.fromkeys("addr", "Saint pauls, QLD")
# d will be considered only once
print(ex_1)

# If one argument is passed using .fromkeys()
ex_1 = {}.fromkeys(["addr"])
# then the 2nd arg is considered by default as NONE
print(ex_1)


# .pop() method
# method does the same thing to dictionaries that it does to lists,
# it removes an item where an item in a dictionary is a key value pair.
# here the dictionary cannot be empty
ex_2 = {"make": "Honda", "model": "civic", "year": 2016}
# remove "model": "civic"
popped = ex_2.pop("model")  # when the key is called for popping
# it's value is also popped
print(ex_2)
print(popped)   # this says what value of the key is popped

# .popitem() method
# it is a method which allows you to remove the last key value pair
# from a dictionary without having to give it an argument.
# but is applicable only for 2.7 python
# For 3 and above version, some random key value will be removed
ex_3 = {"name": "Sai", "age": 26, "occupation": "IT", "workplace": "E block"}
ex_3.popitem() # last key value item will be popped
print(ex_3)

# Dictionary Methods 3
# .clear() method
# just removes everything from a dictionary that it is called on,
# resulting in an empty dictionary,
# the clear method takes no arguments.
ex_1 = {1: "India", 2: "England", 3: "Wales", 4: "USA"}
print(ex_1)
ex_1.clear()
print(ex_1)

# .copy() method
# his method helps to overcome the problem of referencing,
# therefore it makes the dictionary as immutable
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_year)
people = birth_year     # dictionary is assigned to the variable people
people[1982] = "madeline"   # changes are done in people variable
print(birth_year)   # changes will be reflected in the dictionary also
# The above one is te problem
# so to overcome this copy() is used
birth_year = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_year)
people = birth_year.copy()     # a copy f the dic is maintained
people[1982] = "madeline"   # changes are done in people variable only
print(birth_year)   # changes will not be reflected in the dictionary also


# .update() method
# this method allows us to add key value pairs
# from one dictionary to another or
# overwrite the values of existing keys in a dictionary
# with values from another dictionary.
city_info = {"country": "Canada", "provinces": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
# add population to the city_info dictionary
city_info.update(population)
print(city_info)
print(population)   # this dictionary data will not be changed

city_info = {"country": "Canada", "provinces": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
# add population to the city_info dictionary
city_info.update(population)
city_info["population"] = 3000000
print(city_info)    # data of population will be varied
city_info.update(population)
print(city_info)   # the old dic data of population will be over-written

# Exercise of introduction in dictionary
val_1 = {"name": "Sayee",
         "age": 26,
         "occupation": "Business",
         "education": "Masters",
         "location": "Australia"}
print(val_1["occupation"])
print("education" in val_1)
print("music" not in val_1)
print("age" not in val_1)

# Exercise of Dictionary 1 methods
pop_music = {"Queen": "Bohemian Rhapsody",
             "Bee Gees": "Stayin' Alive",
             "U2": "One",
             "Michael Jackson": "Billie Jean",
             "The Beatles": "Hey Jude",
             "Bob Dylan": "Like A Rolling Stone"}
print(len(pop_music))
print(pop_music.keys())
for key in pop_music.keys():
    print(key)
print(pop_music.values())
for key, value in pop_music.items():
    print(key, value)
print(pop_music.get("Promise of the Real", "Promise of the Real is not found"))


# Dictionary method 2 exercise
dictionary_0 = {}.fromkeys("bcdefghijklmnopqrstuvwxy", "constant")
print(dictionary_0)
for key, value in dictionary_0.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac",
                   "Burger King": "Whopper",
                   "Chick-fil-A": "Original Chicken Sandwich"}
popped = fast_food_items.pop("McDonald's")
print(popped)

fast_food_items.popitem()
print(fast_food_items)

# Dictionary method 3 exercise
internet_celebrities = {"DrDisrespect": "YouTube",
                        "ZLaner": "Facebook",
                        "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)
celebs = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(celebs)

# the .setdefault() method
# This allows to give values to keys if they are not found in dictionary
computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
# if a key is not found, one way to add items in the dictionary
if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"

print(computers)
# Another method is that to use .setdefault method
# if the key HP is not there in the dictionary
# then this method will help to add this item in the dictionary
computers.setdefault("HP", "HP Elite")
print(computers)

# if the same key is searched in the dictionary but it has different values
# this does not allow this method to change the value of that key
# Also this does not create a new item in a dictionary
computers.setdefault("HP", "HP Spectre")
print(computers)

# dict() function
# Helps to create a dictionary in python

# To create a empty dictionary
values = dict()
print(values)

# To create a dictionary
values_1 = dict(a=1, b=2, c=3)  # not need for the character to be in quotes
print(values_1)

# Tuples
# It is a list of items
# they are defined by using parentheses

tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)

# To create a tuple
# First method
tuple_4 = (5, 4, 3, 2, 1)
# Second method - using tuple() function
tuple_5 = tuple([3.14, 2.625, 10])
tuple_6 = tuple("abcde")    # each character of the string is considered as tuple
print(tuple_5)
print(tuple_6)

# Use dictionary for defining a tuple
tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple_7)

# Tuples items are accessed by using index numbers
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])   # 3 is accessed
print(tuple_8[:3])  # slicing of tuple
print(tuple_8[2:7])
print(tuple_8[6:])

# tuples are immutable data
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tuple_8[0] = "a"

# long lines in tuples can be divided and shown
# some tuple's which does not require to change its values are
tuple_9 = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")
tuple_10 = ("Fall", "Summer", "Spring", "Winter", "Monsoon")
tuple_11 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z")

# tuples occupy less space in memory
# tuple and list which holds the same value
tuple_12 = (1, 3, 5)
list_1 = [1, 3, 5]
# by using _sizeof_ method,
# we know how much memory both have occupied
print(tuple_12.__sizeof__())
print(list_1.__sizeof__())

# One major use of tuple is to
# provide two key terms for a single value in a dictionary
occupation = {("Angus", "Young"): "musician",
              ("Richard", "Branson"): "entrepreneur"}
seven_wonders = {("N", "E"), "Egypt"}   # two key terms are given

# iterating the values of tuple
major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

# iteration performed by using for loop
for city in major_cities:
    print(city)

# iteration performed by using while loop
count = 0
print("\n")
while count < len(major_cities):
    print(major_cities[count])
    count += 1

# reverse the iteration
backwards = len(major_cities) - 1
print("\n")
while backwards >= 0:
    print(major_cities[backwards])
    backwards -= 1

# tuple slicing by using slice
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[::3])  # slices to the stride length of 3
print(tuple_8[1::2])    # evens only
print(tuple_8[7::-1])   # backward from 8
print(tuple_8[8::-2])   # odds only --> backwards

# nested tuple
# we can declare different sets of tuple in a single tuple
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
# even this type of nesting is also accepted in python
nested_1 = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested_1[4])  # to access a tuple set with in a tuple
# to access a particular value from a tuple set with in a tuple
print(nested_1[5][1])

# count() method
repeat = (7, 3, 3, 3, 0, 1, 7, 0, 0)
# it counts how many times a particular appears
# in the tuple set
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(1))
print(repeat.count(0))

# index()
# It is used for finding the index number of a particular value in a tuple
ints = (1, 1, 7)
print(ints.index(7))
print(ints.index(1)) # since multiple instances of 1 os there in the tuple
# the first call position of that instance is printed as output

# introduction to sets
# A set is a data type which stores a collection of items similar to list.
# To create a set - there are two ways

set_1 = {9, 8, 8, 8, 7, 6}    # first way - set literal
set_2 = set({"a", "b", "a", "c", "d", "e"})  # second way - using set()
print(set_1)
print(set_2)

# to define a empty set
set_3 = set()
print(set_3)
# we use a range to declare the set
set_3 = set(range(1, 12, 2))
print(set_3)

# set can hold items of different data types
set_4 = {"a", 3.14, 18, True}
print(set_4)

# It is not possible to access the items of sets
# by using their index values
set_5 = {3, 6, 9, 12, 15}
for num in set_5:
    print(num)
# to check whether a value is there in a set - in is used
print(12 in set_5)  # boolean values will be written as output
print(5 in set_5)

# set function use
# it avoids duplicated data from a collection
cities = ["Chennai", "Delhi", "Bombay", "Sydney",
          "Melbourne", "Brisbane", "Chennai", "Sydney"]
print(set(cities))
print(len(cities))
print(list(set(cities)))
print(len(list(set(cities))))

# set methods
# .add() - takes any data type as its item argument
# and adds that when a set it called
science = {"Biology", "physics", "Chemistry"}
science.add("Botany")
science.add("Biology")  # nothing in the set list will be changed
print(science)

# .remove()
# removes a item from the set which is called on
fruits = {"banana", "orange", "apple", "tomato"}
fruits.remove("tomato")
print(fruits)

# .discard()
# it does the same thing as like remove();
# only difference is that it will
# not throw an error message when a value is not there in a set
# But .remove() will throw an error message when a value is not there in a set
fruits = {"banana", "orange", "apple", "tomato"}
fruits.discard("pear")  # pear is not there in the list
print(fruits)   # the set values will not be changed
fruits.discard("apple")
print(fruits)

# .copy()
# it just copies the set and keep it in memory
mountains = {"Everest", "Kilimanjaro", 'Fuji'}
set_2 = mountains.copy()
print(set_2 is mountains)   # checks whether both the sets are same
# it will be resulted as "False", but if you check the values of set_2
print(set_2)    # it holds the same value of mountains

# .clear()
# it clears the entire set and accepts no arguments
mountains = {"Everest", "Kilimanjaro", 'Fuji'}
print(mountains)
mountains.clear()
print(mountains)

# .union()
#  it helps to combine the items of two different sets in to single set
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.union(set_2)
print(set_3)
# union can be performed by using | character
set_3 = set_1 | set_2

# .intersection()
# This allows to find out what items that two sets have in common
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.intersection(set_2)
print(set_3)
# this can also be done by using "&"
set_3 = set_1 & set_2
print(set_3)

# .difference()
# the common items of two sets will be removed or subtracted from the set
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.difference(set_2)
print(set_3)
set_3 = set_2.difference(set_1)
print(set_3)
# this can also be done by using "-" symbol
set_3 = set_1 - set_2
print(set_3)
set_3 = set_2 - set_1
print(set_3)
# set comprehension
# an advance way for creating a set
# set comprehension in integer
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

# set comprehension in string
# the characters of the string are iterated
comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)
# sets cannot have duplicates, so A and L will appear only one time