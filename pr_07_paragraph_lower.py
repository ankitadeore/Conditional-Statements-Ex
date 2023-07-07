'''write a program to find out whether a given post is talking "Ankita" or not'''

post=input("Write a paragraph\n\t")


if "ankita" in post.lower():
    print("Ankita is present in the paregraph")
else:
    print("Ankita is not present in the paregraph")


