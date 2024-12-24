# num = int(input("Please enter the number : "))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("*"*(2*i-1),end="")
#     print(" ")
    
Num_1 = int(input("Please enter the number : "))
for i in range(1, Num_1+1):
    if(i==1 or i==Num_1):
        print("*"*Num_1)
    else:
        print("*",end="")
        print(" "*(Num_1-2),end="")
        print("*",end="")
    print("")