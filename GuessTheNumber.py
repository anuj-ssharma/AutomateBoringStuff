import random

#guess a number
secretNumber = random.randint(1,20)

for guessTaken in range(1,7):
    guess = int(raw_input("Guess the number ... "))
    if guess > secretNumber:
        print "High"
        continue
    elif guess < secretNumber:
        print "Low"
        continue
    else:
        break

if guess == secretNumber:
    print "Guessed right in ", guessTaken
else:
    print "Better luck next time"
