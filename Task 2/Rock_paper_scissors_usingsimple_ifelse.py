import random
while True:
                a= print('''1= rock
2=Paper
3= Scissor''')
                b= int(input("enter 1,2 or 3"))
                c=random.randint(1,2) # will choose any no 1,2 or 3
                if b==1 and c==2:
                                print("user loses")
                                print("rock loses from paper")
                elif b==2 and c==3:
                                print("user loses")
                                print("paper loses from scissor")
                elif b==3 and c==1:
                                print("user loses")
                                print("scissor loses from rock")
                elif b==1 and c==3:
                                print("user wins")
                                print("rock wins from scissors")
                elif b==2 and c==1:
                                print("user wins")
                                print("paper wins from rock")
                elif b==3 and c==2:
                                print("user wins")
                                print("scissors wins from paper")
                else :
                                print("tie")
                d=input("do you want to continue yes =y or no=n") #for continuation of while loop
                if d.lower()!='y':
                                break
                            #breaks the while loop
                else:
                                continue 
                            #will lead to execution of loop again