import os

print("Which action you want to perform? \n 1.Shutdown \n 2.Logoff \n 3.Restart \n 4.None")
option = input("\n Enter your option{1/2/3/4} : ")

if (option == 1):
    os.system("Shutdown /s")
elif (option == 2):
    os.system("Logoff /l")
elif (option == 3):
    os.system("Restart /r")
else:
    print("Doing Nothing")



