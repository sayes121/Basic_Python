Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #How to start programming
>>> print('Hello World')
Hello World
>>> 
>>> #We are practising Python using IDLE interactive window and text editor window is used for running a chuck of python scripts
>>> 
>>> #Chapter 1 - Variable, datatype and Expressions
>>> 
>>> #EXPRESSION
>>> 2+2
4
>>> 2
2
>>> 5-3
2
>>> 3*7
21
>>> #Mul is not done by 'x' symbol
>>> 3 x 7
SyntaxError: invalid syntax
>>> 22/7
3.142857142857143
>>> # Order of operation is P- M - D - A - S
>>> 2+3
5
>>> 2+3*6
20
>>> (2+3)*6
30
>>> (5-1)*((7+1)/(3-11))
-4.0
>>> (5-1)*((7+1)/(3-1))
16.0
>>> 
>>> 
>>> 
>>> 
>>> #DATATYPE
>>> 
>>> #Integer
>>> -2
-2
>>> 30
30

#Float
3.14
3.14
42
42
42.0
42.0

# 42 is int and 42.0 is float

#String
'Hello World'
'Hello World'

# String Concatenation
'Alice' + 'bob'
'Alicebob'


#string Concatenation and string repetition
'Alice' * 3
'AliceAliceAlice'
'Hello' + '!' * 10
'Hello!!!!!!!!!!'


#VARIABLES
# stores values in the computer memory - Lableing a values

Spam = 42
# to print the value if Spam
Spam
42
Spam = 'Hello'
Sapm + ' World'
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    Sapm + ' World'
NameError: name 'Sapm' is not defined
Spam + ' World'
'Hello World'
spam
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    spam
NameError: name 'spam' is not defined. Did you mean: 'Spam'?
Spam
'Hello'


#Overriding the Variable
Spam = 'Goodbye'
Spam + ' World'
'Goodbye World'
# the old value is tosed down and replaced by the new value


# Statement with expression

Spam = 2+2
Spam
4
Spam = 10
Spam = Spam +1
Spam
11

