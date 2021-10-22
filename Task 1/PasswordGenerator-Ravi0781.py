import string
import random
n = int(input("Enter the size of password you need"))
print("Here is a list of password suggestion you can use: \nChoose the one that suits you best.")
def ran_pas(length):
    pas = "".join(random.choice(string.ascii_letters + string.digits)for x in range(length))
    print(pas)
for x in range(5):
    ran_pas(n)
