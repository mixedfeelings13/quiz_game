print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! you want to play, let's play :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does HDD stand for? ")

if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got a " + str((score/5) * 100) + "%" + " which means that...")

if (score == 5):
    print("You got all the questions correct! You are a computer genius!")
elif (score == 4):
    print("You got 4 questions correct! You are a computer expert!")
elif (score == 3):
    print("You got 3 questions correct! You are a computer nerd!")
elif (score == 2):
    print("You got 2 questions correct! You are a computer newbie!")
elif (score == 1):
    print("You got 1 question correct! You definitely need to study!")
else:
    print("You got 0 questions correct! You are a noob noob!")