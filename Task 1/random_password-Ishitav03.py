import random
import string

print ('This is a random password generator.')

length= int(input('\n Enter the length of password : '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)
password = "".join(temp)
print(password)