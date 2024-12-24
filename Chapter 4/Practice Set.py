# 01 Write a program to store seven fruits in a list entered by the users.
fruits =[]
f1= input("Please enter the 1st Fruit : ")
fruits.append(f1)
f2 = input("Please enter the 2nd Fruit : ")
fruits.append(f2)
f3 = input("Pleae enter ther 3rd Fruit : ")
fruits.append(f3)
f4 = input("Please enter the 4th Fruit : ")
fruits.append(f4)
f5 = input("Please enter the 5th fruit : ")
fruits.append(f5)
f6 = input("Please enter the 6th Fruit :")
fruits.append(f6)
f7 = input("Please enter the 7th Fruit : ")
fruits.append(f7)
print("You entered Fruits name is ",fruits)

# 02 Write a program to accept marks of 6 studetns and display them in a sorted numbers.
marks = []
student_1 = int(input("Please enter the 1st students marks : "))
marks.append(student_1)
student_2 = int(input("Please enter the 2nd students marks : "))
marks.append(student_2)
student_3 = int(input("Please enter the 3rd students marks : "))
marks.append(student_3)
student_4 = int(input("Please enter the 4th students marks : "))
marks.append(student_4)
student_5 = int(input("Please enter the 5th students marks : "))
marks.append(student_5)
student_6 = int(input("Please enter the 6th students marks : "))
marks.append(student_6)
marks.sort()
print(marks)

# 03 Check that a tupple type cannot be changed in python.
value =(33,55,66,"Ramuk ")
value[3]="Nira"

# 04 Write a program to sum a list with 4 numbers.
List = [34,54,54,45,65]
print(sum(List))

# Write a program to count the number of zero in the following numbers.
List_1 =(0,1,2,2,2,2,0,0,0,1,2)
value=List_1.count(2)
print(value)
