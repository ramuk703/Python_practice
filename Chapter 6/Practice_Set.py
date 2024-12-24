# 01 Write a program to find the greatest of Four number entered by the users.
# Num_1 = int(input("Please enter the 1st Number : "))
# Num_2 = int(input("Please enter the 2nd Number : "))
# Num_3 = int(input("Please enter the 3rd Number : "))
# Num_4 = int(input("Please enter the 4th Number : "))

# if(Num_1>Num_2 and Num_1>Num_3 and Num_1>Num_4):
#     print("Greatest Number is : ", Num_1)
    
# elif(Num_2>Num_1 and Num_2>Num_3 and Num_2>Num_4):
#     print("Greatest Number is : ", Num_2)
    
# elif(Num_3>Num_1 and Num_3>Num_2 and Num_3>Num_4):
#     print("Greatest Number is : ", Num_3)

# elif(Num_4>Num_1 and Num_4>Num_2 and Num_4>Num_3):
#     print("Greatest Number is :",Num_4)
    
# 02 Write a program to find out without a student has passed or failed if it requirs total 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# marks_1 = int(input("Please enter the Marks 1 : "))
# marks_2 = int(input("Please enter the Marks 2 : "))
# marks_3 = int(input("Please enter the Marks 3 : "))

# total_percentage =(100*(marks_1+ marks_2+marks_3))/300

# if(total_percentage>=40 and marks_1>=33 and marks_2>=33 and marks_3>=33):
#     print("Your are pass",total_percentage)
    
# else:
#     print("Your are fail please try again next year",total_percentage)
    
# 03 A spam message
# par_1 ="Hii I am Ramuk from Dondlo Bagodar Giridih Jharkhand pine 825322"
# par_2 ="Wher are you now in currently"
# par_3 ="I am Nira From Bhopal and you"
# par_4 ="No i am a student of Icfai University Jharkhand"
# message = input("Please enter the comment :" )
# if((par_1 in message) or (par_2 in message) or (par_3 in message) or (par_4 in message)):
#     print("This message is a spm")
    
# else:
#     print("This message is a not spam")
    
# 04 
# user_name = input("Please enter your user name : ")
# if(len(user_name)<10):
#     print("your username contains less than 10 characters")
    
# else:
#     print("All is well")
    
# 05 find list name
# List =["Ramuk Kumar", "Nira Mahto","Mukesh Kumar","Guddi"]
# name = input(("Please enter your name : "))
# if(name in List):
#     print("Your Name is search in the List",name)
    
# else:
#     print("Your Name is not in the List",name)
    
# 06 Grade Program
# marks = int(input("Please enter your marks : "))
# if(marks<=100 and marks>=90):
#     Grade = "Ex"
    
# elif(marks<=90 and marks>=80):
#     Grade="A"
# elif(marks<=80 and marks>=70):
#     Grade="B"
# elif(marks<=70 and marks>=60):
#     Grade = "C"
# elif(marks<=60 and marks>=50):
#     Grade = "D"
# print("Your Grade Is : ",Grade)

# 07 Search in List post
post = input("Please enter your posta : ")
if("Ramuk Kumar" in post):
    print("This paragraph talking about Ramuk Kumar")
    
else:
    print("This is not in paragraph")