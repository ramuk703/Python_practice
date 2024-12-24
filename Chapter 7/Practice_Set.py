# 01 Table
num = int(input("Please enter the Number : "))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
    i+=1
    
# 02 Find List name
List =["Rajesh Kumar", "Rani Kumar","Rahul Kumar", "Ramesh Kumar","Mukesh Kumar"]
for name in List:
    if(name.startswith("R")):
        print(f"Hello {name}")
    
# 03 From While loop printing Table
Num = int(input("Please enter the Number : "))
i=1
while(i<11):
    print(f"{Num} X {i} = {Num*i}")
    i+=1
    
# 04 Check Prime or not Prime Number
Num_1 =int(input("Please enter the Number : "))
for i in range(2, Num_1):
    if(Num_1%i)==0:
        print("is not Prime Number")
        break
else:
    print("Nubmer is prime")

# 05 print Natural Number
Num_2 =int(input("Please enter the Number : "))
i =1
sum =0
while(i<=Num_2):
    sum+=i
    i+=1
print(sum)

# 06 Write a program to find  Factorial number
Num_4 =int(input("Please enter the Number Your find the factorial : "))
factorial=1
for i in range(1, Num_4+1):
    factorial=factorial*i
    print(f"Your Factorial Number {Num_4} is{factorial}")
    