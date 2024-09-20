"""The Input Function"""

name = input("What is your name? ")
age = int(input("How old are you? "))
location = input("What is your current location ")
message = (f"Hello {name}, you are {age} years old and live in {location}.")
print(message, end = "\n")
