print("welcome to Hana and Mashael's game")
print("lets guess Mashael's favorite genre")
for x in range (3):
    guess = input("what is your guess?")
    #print(x)
    #print(guess)
    if guess == "horror" or guess== " horror":
        print("correct")
        break
    else:
        print("try again")

print("what do you think is Mashael's favorite movie?")
print("is it hush or the conjuring or IT?")
for x in range (1):
    guess = input("what is your guess?")
    if guess == "hush":
        print("you won!! lets start the next round")
        break
    else:
        print("game over")