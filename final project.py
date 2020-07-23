print("welcome to Hana and Mashael's game")
print("lets guess Mashael's favorite genre")
for x in range (3):
    guess = input("what is your guess?")
    #print(x)
    #print(guess)
    if guess == "horror" or guess== " horror":
        print("correct")
        print("\U0001f600","\U0001f600")
        break
    else:
        print("try again")
        print("\U0001F606","\U0001F606")

print("what do you think is Mashael's favorite movie?")
print("is it hush or the conjuring or IT?")
for x in range (1):
    guess = input("what is your guess?")
    if guess == "hush":
        print("you won!! lets start the next round")
        print("\U0001f600","\U0001f600")
        break
    else:
        print("game over")
        print("\U0001F606","\U0001F606")


print("time to guess Hana's favorite genre?")
for x in range (3):
    guess = input("what is your guess?")
    if guess == "drama":
        print("yes!!")
        print("\U0001f600","\U0001f600")
        break
    else:
        print("try again")
        print("\U0001F606","\U0001F606")

print("now lets guess Hana's favorite movie")
print("is it, the fault in our stars or me before you or wonder?")
for x in range (1):
    guess = input("what is your guess?")
    if guess == "wonder":
        print("you won!! good job!!")
        print("\U0001f600","\U0001f600")
        break
    else:
        print("game over but good try")
        print("\U0001F606","\U0001F606")

        #the emojis were used from this website https://www.geeksforgeeks.org/python-program-to-print-emojis/

