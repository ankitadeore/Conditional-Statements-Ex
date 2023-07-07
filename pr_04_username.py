"""Write a program to find whether a given username contains less than 10 characters or not"""
username=input("Write a text: ")
length=len(username)

if (length < 10):
    print( "username is less than 10 characters")
else:
    print("username is greater than 10 characters")


