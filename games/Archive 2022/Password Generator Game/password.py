'''
Hi !
this is "random Password Generator
made using Python
'''

#import the necessary modules!
import random
import string
print('\n')
print('                                      Generate Your Own Password !!                                 ')

#input the length of password
length = int(input('\nEnter the length of password: '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random
temp = random.sample(all,length)

#create the password
password = "".join(temp)

#print the password

print('\n')
print('Your Best Suitable Password is -> ')
print(password)