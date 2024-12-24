# First Statement
Num = int(input("Please enter your ATM pin no. : "))

if(Num==9576):
    print("Please enter Your Amount : ")
    st= int(input(""))
    print("Your Transaction is done")
    
# First Statement End

elif(Num==0):
    print("You Entered zero Please type Correct Pin")
    
elif(Num<0):
    print("You Entered Negative Number")
else:
    print("Your Pin is Invalid Please try Again") 