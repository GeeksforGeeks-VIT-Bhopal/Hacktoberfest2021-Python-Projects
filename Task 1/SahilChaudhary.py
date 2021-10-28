import random
import array

Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LCC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
UCC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
Maxlen = int(input("Please input the length of your password:\n"))

# combines all the character arrays above to form one array
COMBINED_LIST = Numbers + UCC + LCC + Symbols

# selecting at least one character from each character set above
random_num = random.choice(Numbers)
random_ucc = random.choice(UCC)
random_lcc = random.choice(LCC)
random_symbol = random.choice(Symbols)

temp_pass = random_num + random_ucc + random_lcc + random_symbol

for x in range(Maxlen - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
# to form the password
Password = ""
for x in temp_pass_list:
    Password = Password + x
print(Password)
