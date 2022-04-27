# Question: A spam comment is defined as a text cotaining following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

# sentence = input("Type the comment: ")

# if("make a lot of money" in sentence):
#     print("it is spam")
# elif("buy now" in sentence):
#     print("it is spam")
# elif("sun=bscribe this" in sentence):
#     print("it is spam")
# elif("click this" in sentence):
#     print("it is spam")
# else:
#     print("it is not spam")


sentence = input("Type the comment: ")

if("make a lot of money" in sentence):
    spam = True
elif("buy now" in sentence):
    spam = True
elif("sun=bscribe this" in sentence):
    Spam = True 
elif("click this" in sentence):
    spam = True
else:
    spam = False

if(spam):
    print("This text is a spam.")

else:
    print("This text is not a spam.")


