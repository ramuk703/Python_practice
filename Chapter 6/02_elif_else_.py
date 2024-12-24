age = int(input("Please enter your age : "))

if(age>=18):
    print("You are Eligible for Vote")
elif(age<0):
    print("You are Entering negative value")
elif(age==0):
    print("You are entering zero ")
else:
    print("Your are not Eligible for Vote")
    
print("Program is Finished")