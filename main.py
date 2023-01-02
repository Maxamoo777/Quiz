# This is the welcome message.
print("Welcome...TO THE IMPOSSIBLE QUIZ!")
score = 0

answering = True
answer = input("2+2=?")

while answering == True:
    if answer == "4":
        score = score + 1
        print("Correct! Your score is now " + str(score) + "!")
        answering = False
    else:
        print("Incorrect.")
        answer = input("2+2=?")


answering = True
answer = input("7x7=?" )

while answering == True:
    if answer == "49":
        score = score + 1
        print("Correct! Your score is now " + str(score) + "!")
        answering = False
    else:
        print("Incorrect.")
        answer = input("7x7=? ")


answering = True
answer = input("3/6=? ")

while answering == True:
    if answer == "0.5":
        score = score + 1
        print("Correct! Your score is now " + str(score) + "!")
        answering = False
    else:
        print("Incorrect.")
        answer = input("3/6=? ")  