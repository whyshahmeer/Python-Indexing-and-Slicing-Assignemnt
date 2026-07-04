print("USING BASIC INDEXING IN THE FIRST FOUR QUESTIONS\n")
# QUES1:
# word = "Artificial"
# Print:
# - First character
# - Last character
# - Third character
# - Second last character

word = "Artificial"

print("Word:", word)

print("\nFirst character:")
print(word[0])

print("\nLast character:")
print(word[-1])

print("\nThird character:")
print(word[2])

print("\nSecond Last character:")
print(word[-2])

# Question 2
# Given:
# country = "Pakistan"
# Using indexing only, print:
# P
# a
# n

country = "Pakistan"

print("\nCountry:", country)

print("\nFirst character:")
print(country[0])

print("\nSecond character:")
print(country[1])

print("\nLast character:")
print(country[7])

# Question 3
# Given:
# numbers = [15, 28, 34, 49, 56, 78]
# Print:
# - First element
# - Fourth element
# - Last element

numbers = [15, 28, 34, 49, 56, 78]

print("\nList:", numbers)

print("\nFirst element:")
print(numbers[0])

print("\nFourth element:")
print(numbers[3])

print("\nLast element:")
print(numbers[5])

# Question 4
# Given:
# fruits = ["Apple", "Banana", "Orange", "Mango", "Peach"]
# Print Banana, Mango, and Peach using indexing only.

fruits = ["Apple", "Banana", "Orange", "Mango", "Peach"]

print("\nFruits:", fruits)

print("\nSecond fruit:")
print(fruits[1])

print("\nFourth fruit:")
print(fruits[3])

print("\nFifth fruit:")
print(fruits[4])

print("\n---Basic Index ENDED---\n")

print("USING NEGATIVE INDEXING IN QUESTIONS 5-8\n")

# Question 5
# Given:
# language = "Programming"
# Using negative indexing, print:
# - Last character
# - Second last character
# - Fifth last character

language = "Programming"

print("Language:", language)

print("\nLast character:")
print(language[-1])

print("\nSecond Last character:")
print(language[-2])

print("\nFifth Last character:")
print(language[-5])

# Question 6
# Given:
# colors = ["Red", "Green", "Blue", "Black", "White"]
# Print White, Black, and Green using negative indexing only.

colors = ["Red", "Green", "Blue", "Black", "White"]

print("\nColors:", colors)

print("\nLast color:")
print(colors[-1])

print("\nSecond Last color:")
print(colors[-2])

print("\nFourth Last color:")
print(colors[-4])

# Question 7
# Given:
# marks = [78, 85, 91, 66, 74, 88, 95]
# Print the last, third last, and fifth last mark.

marks = [78, 85, 91, 66, 74, 88, 95]

print("\nMarks:", marks)

print("\nLast mark:")
print(marks[-1])

print("\nThird Last mark:")
print(marks[-3])

print("\nFifth Last mark:")
print(marks[-5])

# Question 8
# Given:
# sentence = "Python is amazing"
# Using negative indexing, print:
# g
# n
# P

sentence = "Python is amazing"

print("\nSentence:", sentence)

print("\nLast character:")
print(sentence[-1])

print("\nSecond Last character:")
print(sentence[-2])

print("\nSixteenth Last character:")
print(sentence[-17])

print("\n---Negative Index Ended---\n")

print("USING BASIC SLICING IN QUESTIONS 9-11\n")

# Question 9
# Given:
# numbers = [10,20,30,40,50,60,70,80]
# Print the first four and last four numbers using slicing.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Numbers:", numbers)

print("\nFirst four numbers:")
print(numbers[:4])

print("\nLast four numbers:")
print(numbers[-4:])

# Question 10
# Given:
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Print the first 10 letters and the last 10 letters.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\nAlphabet:", alphabet)

print("\nFirst 10 letters:")
print(alphabet[:10])

print("\nLast 10 letters:")
print(alphabet[-10:])

# Question 11
# Given:
# cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta", "Multan"]
# Print the first three cities and the last two cities using slicing.

cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta", "Multan"]

print("\nCities:", cities)

print("\nFirst three cities:")
print(cities[:3])

print("\nLast two cities:")
print(cities[-2:])

print("\n---Basic Slicing Ended---\n")

print("USING STEP SLICING IN QUESTIONS 12-15\n")

# Question 12
# Given:
# numbers = [1,2,3,4,5,6,7,8,9,10]
# Print every second number and every third number.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Numbers:", numbers)

print("\nEvery second number:")
print(numbers[::2])

print("\nEvery third number:")
print(numbers[::3])

# Question 13
# Given:
# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Print every second and every third letter.

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\nText:", text)

print("\nEvery second letter:")
print(text[::2])

print("\nEvery third letter:")
print(text[::3])

# Question 14
# Given:
# values = [5,10,15,20,25,30,35,40,45,50]
# Print elements at even indices and odd indices.

values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("\nValues:", values)

print("\nElements at even indices:")
print(values[::2])

print("\nElements at odd indices:")
print(values[1::2])

# Question 15
# Given:
# word = "COMPUTERSCIENCE"
# Print every second character starting from index 1.

word = "COMPUTERSCIENCE"

print("\nWord:", word)

print("\nEvery second character starting from index 1:")
print(word[1::2])

print("\n---Step Slicing Ended---\n")

print("USING Advanced Indexing and Slicing IN QUESTIONS 16-18\n")

# Question 16
# Given:
# word = "PYTHON"
# Reverse the string using slicing.

word = "PYTHON"

print("Word:", word)

print("\nReversed string:")
print(word[::-1])

# Question 17
# Given:
# numbers = [5,10,15,20,25,30,35]
# Reverse the list using slicing.

numbers = [5, 10, 15, 20, 25, 30, 35]

print("\nNumbers:", numbers)

print("\nReversed list:")
print(numbers[::-1])

# Question 18
# Given:
# message = "Python Programming Language"
# Using slicing only, print:
# 1. Python
# 2. Programming
# 3. Language
# 4. nohtyP
# 5. The last 8 characters
# 6. Every second character from the entire string

message = "Python Programming Language"

print("\nMessage:", message)

print("\n1. Python:")
print(message[:6])

print("\n2. Programming:")
print(message[7:18])

print("\n3. Language:")
print(message[19:])

print("\n4. nohtyP:")
print(message[:6][::-1])

print("\n5. Last 8 characters:")
print(message[-8:])

print("\n6. Every second character:")
print(message[::2])


print("\n---Advanced Indexing and Slicing---\n")

print("FINAL QUESTIONS: ADVANCED SLICING\n")

# Question 19
# Given:
# data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Without using loops:
# 1. Print the first 10 characters.
# 2. Print the alphabets only.
# 3. Print every second character.
# 4. Print the string in reverse.
# 5. Print characters from index 5 to 20.
# 6. Print every third character from index 3 to the end.
# 7. Print the last 10 characters.
# 8. Print everything except the first and last character.

data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Data:", data)

print("\n1. First 10 characters:")
print(data[:10])

print("\n2. Alphabets only:")
print(data[10:])

print("\n3. Every second character:")
print(data[::2])

print("\n4. String in reverse:")
print(data[::-1])

print("\n5. Characters from index 5 to 20:")
print(data[5:21])

print("\n6. Every third character from index 3 to the end:")
print(data[3::3])

print("\n7. Last 10 characters:")
print(data[-10:])

print("\n8. Everything except the first and last character:")
print(data[1:-1])

