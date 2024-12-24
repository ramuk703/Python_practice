# 01 Write a program using functins to find greatest of three numbers.
# def Num(num_1,num_2,num_3):
#     if(num_1>num_2 and num_1>num_3):
#         return num_1
#     elif(num_2>num_1 and num_2>num_3):
#         return num_2
#     elif(num_3>num_1 and num_3>num_2):
#         return num_3
    
# num_1 = 12
# num_2 = 353
# num_3 =33

# print(Num(num_1,num_2,num_3))

# 02 Write a python program using function to convert Celsius to Fahrenheit.
# def f_to_c(f):
#     return   5*(f-32)/9
# f = int(input("Please enter the tempreature in Celsius : "))
# c= f_to_c(f)
# print(f"{round(c,2)}°C")

# 03 How do you prevent a python print() functio to print a new line at the end.
# print("A")
# print("B")
# print("c", end="")
# print("D",end="")
   
# 04 Write a recursive function to calculate the sum of first n natural numbers.
# def natural(num):
#     if(num==1):
#         return 1
#     return natural(num-1)+num
# print(natural(5  ))
import numpy as np
a=np.array([[2,3,4,5,6],[4,5,6,2,8]])
print(a[2:4,0:2 ])
