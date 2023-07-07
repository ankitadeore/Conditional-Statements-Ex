'''A spam comment is defined as a text containing following keywords:
"Make a lot of money ", "buy now","subscribe this",
"click this " write a program to detect these spams'''
comment=input("Enter some text here:")


if("Make a lot of money"in comment):
     spam = True
elif("buy now"in comment):
     spam = True
elif("subscribe this"in comment):
     spam = True
elif("click this"in comment):
    spam = True

else:
    spam = False
if(spam):
    print("This comment is spam ")
else:
    print("This comment is not spam")



