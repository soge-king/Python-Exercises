# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:30:02 2024
covering chap 6
@author: Francois Martinie
"""
"""
                string lib for python

str.capitalize()
str.center()
str.endswith()
str.find()
str.strip() st.lstrip() str.rstrip()
str.replace()
str.lower()
str.upper()

"""
#basic str actions, working with the index and slicing
word = 'INDEX'
y = 1
w = word[2]
x = word[2+y]
print(w)
print(x)
print(word[0:2])
print(word[2:4])
for n in "banana":
    print(n)

if 'N' in word:
    print('true')
else:
    print('false')
if 'M' in word:
    print('true')
else:
    print('false')
#this is an example of using for as a logic op, similar to bool
"""

another example is
if 'a' in fruit:
    print("Found it!")")
"""


#searching for substring using the find func
word1 = "bananana"
i = word1.find("na")
print(i)

 #lowercase and upper case
zap = word.lower()
print(zap)
print('HELLO THERE'.lower())
# print('HELLO THERE'.lower([1:5]))    WRONG
print('amigo'.upper())
 
dir(word)
type(word)

#stripping space

greet = ' Hello there Neighbor '
u = greet.lstrip()
e = greet.rstrip()
a = greet.strip()
print(u)
print(e)
print(a)



#prefixes
line = "Hello there my friend"
line.startswith('h')  #returns false
line.startswith('Hello')  #returns true



data = 'myemail@gmail.com Sat Jan 2 5:30:01 2024'
atpost = data.find('@')
print(atpost)
mail = data.find(' ',atpost)
print(mail)
host = data[atpost+1 : mail]
print('host:',host)


"""

extra:
    
    


string.ascii_letters

    The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

string.ascii_lowercase

    The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

string.ascii_uppercase

    The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

string.digits

    The string '0123456789'.

string.hexdigits

    The string '0123456789abcdefABCDEF'.

string.octdigits

    The string '01234567'.

string.punctuation

    String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

string.printable

    String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.

string.whitespace

    A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.

"""
 