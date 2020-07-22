print("time to guess Hana's favorite genre?")
for x in range (3):
    guess = input("what is your guess?")
    if guess == "drama":
        print("yes!!")
        break
    else:
        print("try again")

print("now lets guess Hana's favorite movie")
print("is it, the fault in our stars or me before you or wonder?")
for x in range (1):
    guess = input("what is your guess?")
    if guess == "wonder":
        print("you won!! good job!!")
        break
    else:
        print("game over but good try")