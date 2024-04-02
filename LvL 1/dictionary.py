"""
Created on Mon Jan  10 
covering chap 9
@author: Francois Martinie
Python Dictionaries
"""
'''
Collections are variable sotring variablers. 
Dictionary is a type of collection that stores and labels values, 
while a list is a collection of values with no inherent label, but ordered by an index.

'''

#exm if a list
name = {'jose','maria','fran','lana'}


#exmp of dictionary
dict = {"Fri": 20, "Thu": 6, "Sat": 1}
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9


#example of interactive divctionary using user input
inventory = {}  # Initialize an empty dictionary to store items and amounts

while True:
    try: #to avoid crashes in case od an str where a int should be, the try func is used
        items = input('Enter an item for your inventory (or "done" to finish): ')
        if items == 'done':  break
  # Add the item and amount to the dictionary
        # Check if the names are purely alphabetical
        if not items.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        while True:
            
            try:
                amount = int(input('Enter the amount of the item: '))
                # Check if the amount is non-negative
                if amount < 0:
                    raise ValueError("Amount of items must be non-negative")
                inventory[items] = amount  # Add the item and amount to the dictionary
                break  # Break out of the inner laoop once a valid amount is entered

            except ValueError:
                print("Error with amount:  is not a valid number. Please enter a valid integer.")
                # The loop continues, prompting the user to re-enter the amount     
                
                
#       amount = int(input('Enter the amount of the item: '))
#       if amount<0:
#           raise ValueError("Say the amount of items correctly")
    except ValueError as e:
        print("Error 1-2:", e)
        continue
print('Inventory: ') #if you just print the inventory var, youll get the values and labels but that aint pretty

for item, amount in inventory.items():
    print(f'\n {amount} {item} and,')
print('....thats it, thank you!')
#f' is used for inputing stuff and '{stuff}' is how you insert it in a string       

###################################################################################
friends = {
    'gale': (1.7, 'M'),
    'astarion': (1.6, 'M'),
    'karlach': (2.0, 'F'),
    'wyll': (1.8, 'M'),
    'shadowheart': (1.5, 'F'),
    'lae-zel': (1.6, 'F')
}
#cool thing about dictionaries, they allow a label 
#to have more than one var associated with it
#lets sat you want to add another friend in an if 
#statement, then add this line under the if statment
friends['halsin'] = (2.1, 'M')  


#now your looking for info on a friend in the list
name = input('Who do you need? ')
info = friends.get(name)

if info:
    print(f'Ah yes, {name} is {info[0]}m tall and is {info[1]}.')
else:
    print(f'Sorry, I don\'t have information about {name}.')
#now lets say YOU want to add a companion, then this loop will keep adding to the list
while True:
    add_companion = input("Do you want to add a new companion? (Y/N): ").strip().upper()
    
    if add_companion == 'N':
        break
    elif add_companion == 'Y':
        name = input("What is the name of the companion? ").strip()
        height = float(input("What is the height of the companion (in meters)? ").strip())
        sex = input("What is the sex of the companion (M/F)? ").strip().upper()
        
        friends[name] = (height, sex)
        print(f"{name} added to companions.")
    else:
        print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

print("\nFinal list of companions:")
for name, info in friends.items():
    print(f'{name} - Height: {info[0]}m, Gender: {info[1]}')
    
##########################################
"""
Created on Mon Jan  10
covering chap 10
@author: Francois Martinie
Tuples and Tops
"""

#########################################################################
#tuples  It's a collection of items, 
#just like a list, but tuples are immutable, 
#meaning they cannot be changed after they are created.

x = {'this','is','a','set'} #A set is mutable but does not allow duplicate elements.
y = [1, 2, 3] #this is a list
z = ('this', 'is',' a',' touple') #tuples use () and are immutable
dictionary = {'a': 1, 'b':2, 'c':3} #(name of dic) = {label, value(s)}
#you can make a blank dictionary using (nameofvariable) = dict()


#tuples cant be sorted, appened, reversed, etc. only count and index can be used
#on a tuple

################
#you CAN assign a val or int on a tuple

(g,v) = (4, 'fred')
print(v)
#gives 'fred'

#you can make a list of tuples, like nesting a list in a list
#comparing tuples can be tricky
(1,2,3)<(4,5,6) #checks 1< 4, true then ignores the rest
#if you try with strings then the value of each name is based on the ascii val of the letter
#so for example J>A   


#now you cant change a tuple, but you can organize tupes inside a dictionary
d = {'b':1,'a':2,'c':3,'f':4,'e':5,'g':6,'d':7}
t = (sorted(d.items()))
# the .items func returns a view object that displays a 
#list of dictionary's key-value tuple pairs. 

#now that we can see the values of the tuples in the dict, we can sort the with sorted
print(t)

"""
result:
[('a', 2), ('b', 1), ('c', 3), ('d', 7), ('e', 5), ('f', 4), ('g', 6)]
"""
#now lets try to organize it further, 
#remember im not doing anything to the tuples, just the dictionary
#the tuples are being organized by the first value

for k, v in sorted(d.items()):
    print(k, v)


"""
tuples
a 2
b 1
c 3
d 7
e 5
f 4
g 6
"""
#to make the result be the inverse of what it is then:
lst = [] #make a new list or dic
for k, v in sorted(d.items()): #we organize the list
    newvalue = (v,k) #associate past dict to a new variable(basically copy paste)
    lst.append(newvalue) #we add the variable to the list
lst = sorted(lst, reverse=True) #sort the list again, but in reverse
print(lst) #print reverse list



#we can also sort the dictionary in a limited cap, so if we 
#want we can organize half the list like this
'''
for k,v in lst[:10]:
    print(k,v)

'''


#say i want to fin the most used word in a book

'''
fhand  = open('somebook.txt') #opens the book
counts = dict() #make an empty dictionary 

for line in fhand: #read book like by line
    words = line.split() #remove the white space
    for word in words:  #now read word for word
        counts[word]= count.get(word, 0) +1 #count and store word

'''






