# # 01 Write a program to create a dictionary of Hindi words with values as their English translation, provides user with an option to look it up!

words = {
    "aam":"Mango",
    "annar":"Pomegranate",
    "santra": "Orange",
    "sew":"Apple"
    
}

# word=input("Please enter the word you want to meaning of : ")
# print(words[word])

# # 02 Write a program to input eight numbers form the user and display all the uinque numbers (once).

set_1 =set()
s1 = int(input("Please enter the first number : "))
set_1.add(s1)
s2 = int(input("Please enter the 2nd number : "))
set_1.add(s2)
s3=int(input("Please ente the 3rd number : "))
set_1.add(s3)
s4 = int(input("Please enter the 4th number : "))
set_1.add(s4)
s5 =int(input("Please enter the 5th number : "))
set_1.add(s5)
print(set_1)

# 03 Can we have a set with 18 (int) adn '18' (str) as a value in it?
s1=set()
s1.add(28)
s1.add("28")
print(s1)

# 04 What will be the length of following set S:
s1 = set()
s1.add(10)
s1.add(10.0)
s1.add("20")
print(len(s1))

# 05 s={} what is the type of 's'?
s={}
print(type(s))

# 06 Create an empty dictionary, Allow 4 friends to enter their favorite languages as value and use keys as their names. Assume that the names are uniques.
dic={}
name=input("Please enter the Name : ")
lang=input("Please enter the Lang : ")
dic.update({name:lang})

name=input("Please enter the Name : ")
lang=input("Please enter the Lang : ")
dic.update({name:lang})

name=input("Please enter the Name : ")
lang=input("Please enter the Lang : ")
dic.update({name:lang})

name=input("Please enter the Name : ")
lang=input("Please enter the Lang : ")
dic.update({name:lang})

print(dic)

# 07 If the names of 2 friends are same; what will happen to the program in problem 6