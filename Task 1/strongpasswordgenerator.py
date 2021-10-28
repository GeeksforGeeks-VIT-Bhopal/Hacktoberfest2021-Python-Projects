#strong and nearly uncrackable password generator
a= input ("enter first name with first letter as capital")
b= input ("enter date of birth as DDMMYYYY")
c= input("enter special character to be used")
pas= a[0:2]+c+b
# concatenation is used 
print("password is ", pas)