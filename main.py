# This is the welcome message.
print("Welcome...TO THE IMPOSSIBLE QUIZ!")
score = 0
alive = True
lives = 3

answering = True
answer = input("2+2=? ")

while alive == True:
    while answering == True:
        if answer == "4":
            score = score + 1
            print("Correct! Your score is now " + str(score) + "!")
            answering = False
        else:
            print("Incorrect.")
            lives = lives - 1
            answer = input("2+2=? ")

    answering = True
    answer = input("7x7=? ")

    while answering == True:
        if answer == "49":
            score = score + 1
            print("Correct! Your score is now " + str(score) + "!")
            answering = False
        else:
            print("Incorrect.")
            answer = input("7x7=? ")
            lives = lives - 1
            if lives < 1:
                alive = False

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
            lives = lives - 1
            if lives < 1:
                alive = False

    answering = True
    answer = input("68-45=? ")

    while answering == True:
        if answer == "24":
            score = score + 1
            print("Correct! Your score is now " + str(score) + "!")
            answering = False
        else:
            print("Incorrect.")
            answer = input("68-45=? ")  
            lives = lives - 1
            if lives < 1:
                alive = False

    answer = input("68-45=? ")
    while answering == True:
        if answer == "23":
            score = score + 1
            print("Correct! Your score is now " + str(score) + "!")
            answering = False
        else:
            print("Incorrect.")
            answer = input("68-45=? ")  
            lives = lives - 1
            if lives == 0:
                print ("Your lives are at "+ str(lives) + "sooo.....SAY GOODBYE TO YOUR PROGESS!")
                alive = False
                answering = False
                answer = input("2+2=? ")

print ("Thats it for now,BYE!!!!")