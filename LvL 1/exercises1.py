# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:47:41 2023

@author: User
"""

yername = input('What is your name ?:')

print('Hello',yername,',Now before we begin')



### repeat question till correct answer is given
while True:
    paystyle = input('What is your paystyle, \n Hourly (h) or Fixed Pay (f)?:')
    if paystyle in ['h', 'f']:
        break
    else:
        print("Invalid input. Please try again.")

while True:
    sorm = input('Are you Single (s) or Married (m)?: ')
    if sorm in ['s', 'm']:
        break
    else:
        print("Invalid input. Please try again.")
xpy = 0
taxbrac = 0
###########
#the while true takes care of the error
#demonstrates redundancy if choices arent limited
"""
try:
    er1 = str(yername)
    er2 = str(paystyle)
    er3 = str(sorm)

except:
    print("error, not a word")
    continue
"""
'''
try:
    er4 = float(xh)
    er5 = float(xr)
    er6 = float(xp)
    er7 = float(xpy)
    er8 = float(xpy)
    er9 = float(xm)
    er10= float(donations)
except:
    print('Error, not a number')
    continue       #continue is used to return after bad input
                   #inside a loop
'''
###reduntant code and examples of milti lime comment 
###
if paystyle == 'h':
    
     xh = input("How many hours do you work a week?:")
     xr = input('and what was your rate ?')
     
     if xh > 40:
         otp = (xh-40) * (float(xr)*1.5)
         xp = (xr*xh)+otp
         print('Your overtime is:',xh-40, '\n And your overtime pay is:',otp)
     else:
         xp = float(xh) * float(xr)
     
     xpy = float(xp) * 4 * 12
     print('Your pay is:', xp, ' per week and your yearly Salery is', xpy)

elif paystyle == 'f':
    xm = input('whats your monthly salery ?:')
    xpy = float(xm) * 12
    print('Your pay is:', xm, 'and your yearly Salery is', xpy)

else:
    print("Error")
donations = input('Have you donated any momey ? \n Enter the amount (if not just put 0):')


## see how if statements work
#here there are two if statements, one nested one not                             
if sorm == 'm':
    xpy = xpy/2
    
if xpy <= 11000:
    taxbrac = 0.1
elif xpy <= 44725:
    taxbrac = 0.12
elif xpy <= 95375:
    taxbrac = 0.22
elif xpy <= 182100:
    taxbrac = 0.24
elif xpy <= 231250:
    taxbrac = 0.32
elif xpy <= 578125:
    taxbrac = 0.35
else:
    taxbrac = 0.37

tax = float(xpy) * float(taxbrac) 
taxbracket = taxbrac * 100
totaltax = tax - float(donations)
###
def totalpay(tb,tt):
    print('You are in the ',tb,'% bracket, \n meaning you will be taxed', tt)

totalpay(taxbracket, totaltax)
