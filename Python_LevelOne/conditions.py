# # #theScore = 77
# # print("your score is:", theScore)
# # print("""
# #          Cooo
# #          ooooooooool""")
# theScore = input("enter your score here:")
# if theScore == "abc":
#     print("well done")
# else:
#     print("try again :)")
#
#
# theScore = input("enter your score here:")
# print("you entered", theScore)
# if theScore == "abc":
#     print("well done")
# else:
#     print("try again :)")
#
# theScore = float(input("""
# Checking the following
# <, >, ===
#  Enter a number"""))
# print("you entered- ", theScore)
# int(theScore)
# if theScore == 78:
#
#     print("well done")
# else:
#     print("try again :)")
#     theScore = float(input("""
#     Checking the following
#     <, >, ===
#      Enter a number"""))
#     print("you entered- ", theScore)
#     int(theScore)
#     if theScore ==
#
#         print("well done")
#     else:
#         print("try again :)")

# score = 2
# if score < 30:
#     print("its less than 30") #use indendation , but the first indedation ..spaced must be used in all the blocks of code where idnendaition is necessary
# else:print("ok!")

# rating = int(input("How would you are us? -  0? or 5? "))
# if rating == 0:
#     print("Sorry to hear that :| ")
#     improve_Rating = input("Tell us how we can improve or what went wrong!")
# elif rating == 5:
#     print("Thankyou!!")

##TODO: More scales
rating = int(input("How would you are us? -  0? or 5? "))
if rating == 0:
    print("Sorry to hear that :| ")
    improve_Rating = input("Tell us how we can improve or what went wrong!")
elif rating == 1:
    print("we will defifnetly improve for that rating 1")
elif rating == 2:
    print("we will defifnetly improve for that rating 2")
elif rating == 3:
    print("we will defifnetly improve for that rating 3")
elif rating == 4:
    print("we will definitely improve for that rating 4")

elif rating == 5:
    print("Thankyou! ")
    Rating_good = input("Tell us what you liked the most ")
else: #add colon for else
    print("please enter a value less than 5")
#\ forward slash or line continuation slash
