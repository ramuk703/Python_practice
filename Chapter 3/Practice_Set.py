# 01  Write a python program to display a user entered name followed by Good Afternoon using input() function.

name = str(input("Please enter your name: "))
print("Good Afternoon",name,)
print(f"Good Afternoon {name}")

# 02  Write a program t fill in a letter template given below with name and date.

letter = """Dear Name,
You are selected!
Date"""
print(letter.replace("Name","Ramuk").replace("Date","24-sep-2024"))

# 03 Write a program to detect double space in a string.

name_3  = "Ramuk Kumar  Mahto Dondlo"
print(name_3.find("  "))

# 04 Replace the double space from problem 3 with single spaces. 
name_4 = "Ramuk Kumar  Mahto"
print(name_4.replace("  "," "))

# 05 Write a praogram to format the following letter using escape sequence characters.

Letter = "\"Dear Ramuk \n this python course is nice.Thanks!\""
print(Letter)