'''Write a program which finds out whether a given name is present in the a list or not'''
find_name=["ankita","harry","shipra","satya","yuvaan"]

name=input("Enter the name to check \n")

if (name in find_name):
    print("Your name is present in the given list")
else:
    print("The name is not present in the list")

