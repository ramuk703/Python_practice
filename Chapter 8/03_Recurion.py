def factorial(num):
    if(num==1 or num==0):
        return 1
    return num*factorial(num-1)

num=int(input("Please enter the Number : "))
print(f"Factorial of this number is {factorial(num)}")