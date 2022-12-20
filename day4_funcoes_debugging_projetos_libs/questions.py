#!/usr/bin/env python3

# print("Welcome to the test.")
# input("When you are ready press enter.")

# name = input("name: ")
# print(f"It is nice to meet you {name}")

# color = input("What is yout favorite color?\n")
# print(f"{color} is a great color!")

# input("Describe yourself\n")
# print("Admirable!")

# print("Goodbye.")

def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.")

def ask_questions():
    name = input("name: ")
    print(f"It is nice to meet you {name}")

    color = input("What is yout favorite color?\n")
    print(f"{color} is a great color!")

    input("Describe yourself\n")
    print("Admirable!")

def goodbye():
    print("Goodbye.")

welcome()
ask_questions()
goodbye()