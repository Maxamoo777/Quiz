# This is the welcome message.
print("Welcome...TO THE IMPOSSIBLE QUIZ!")
score = 0

answer = input("2+2=?")
if answer == "4":
    score = score + 1
    print("Correct! Your score is now " + str(score) + "!")

answer = input("7x7=? ")
if answer == "49":
    score = score + 1
    print("Correct! Your score is now " + str(score) + "!")
answer = input("3/6=? ")
if answer == "0.5":
    score = score + 1
    print("Correct! Your score is now " + str(score) + "!")