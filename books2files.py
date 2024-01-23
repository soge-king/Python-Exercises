"""
Created on Mon Jan  8 14:30:02 2024
covering chap 7
@author: Francois Martinie
handeling files
"""

#create the input var for the file name

fname = input('Enter name of the file: ')

try: 
    fhand = open(fname)
except:
    print('Could not find file named:',fname)
    pass 
#can use raise SystemExit if you want to exit the file, if you want to continue
#use pass

    
#quit is used to terminate the program without trace back
#similar to a stop all func
    
    
#handle = open(filename, mode)
camus = open('TheStranger.txt')
print(camus)

#this gives some general data of the file
#error on file name gives traceback
stuff = "Hello \nWorld" #\n new line
print(stuff)
q = len(stuff) #lenght of str
print(q)
"""
exiting a program:
    sys.exit(): 
        This function is part of the sys module, and it raises a SystemExit exception to exit the program. 
        must use "import sys"
    
    quit(): 
        As discussed earlier, quit() is typically used in interactive environments like the Python REPL to exit the interactive session.
    
    os._exit(): 
        This function from the os module immediately terminates the program without performing any cleanup or running exit handlers. 
    
    raise SystemExit: 
        You can manually raise a SystemExit exception to exit the program gracefully
    
    return (in functions or methods): 
        When your code is inside a function or method, you can use the return statement to exit the function and, indirectly, terminate the program if it's the main function being executed.
     pass 
         the pass statement is a null operation or a placeholder. It is a statement that does nothing. It is used when you need a statement in your code for syntactical reasons, but you don't want it to perform any specific action    



"""

#counting the lines in the file, for this i put the book "the stranger" in a txt file
count = 0
for line in camus:
    if line.startswith('While'):    #searching through a file
        print(line)
    if not 'I' in line:
        continue   
#continue just skips this part of the loop and continues to the next iteration
#sort of like a "you've been here before, so just move along" notice
    count = count + 1
print('Total Line Count:',count)
      
#reading the *whole file*

'''
book = camus.read()
print(len(book))
print(book[:20])

with open('TheStranger.txt', 'r') as camus:
    book = camus.read()

this code is similar to the code on the vid but didnt work as intended (for some reason *shrug*)
 so the code after is to do the same job

'''
with open('TheStranger.txt', 'r') as camus:
    book = camus.read()
#We use a with statement to ensure that the file is properly closed after reading.
#We read the content of the file and store it in the book variable.
#We split the book content into lines using split('\n') and count the number of lines.


# Print the total character count and the first 20 characters
print('Total character count:', len(book))
print('First 200 characters:', book[:200])

# Count the lines in the file
lines = book.split('\n')
line_count = len(lines)
print('Line count:', line_count)

#################################################################
"""
Created on Mon Jan  8 14:30:02 2024
covering chap 8
@author: Francois Martinie
Python Lists
"""

#these lists are a collection of many values in a single variable
#similar to an array

fruit = "banana"
x = fruit[1]


friend = ['jose', 'maria', 'juan']  
#for this list, the index always starts at 0 so

print(friend[0])

print(friend[1])

print(friend[2])


"""
Extra:
    
    
    Pass:
        Uses:
            -Placeholder
            -Indentation for Syntatic requirements (if you need an extra func for the structure of the program to work but dont need it to do anything, use pass)
            -Similar to void, as it doenst effect program flow
        Examples:
       def my_function(): 
    # To be implemented later
    pass

if condition:
    # To be filled in
    pass

while some_condition:
    # No action required yet
    pass
 
"""

total = 0
cont = 0 
while True:
    inp = input('Enter a Number:')
    if inp == 'done' : break
    valor = float(inp)
    total = total + valor
    cont = cont + 1
ave = total / cont
print('average:', ave)


###############################

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split() #seperates each word individially, treats all space/tab the same
parts = pieces[3].split('-') #4th word of the list of words, split the word by the '-'
n = parts[1] #second part of the word, being lar@freecodecamp.org

