import random

# Get the upper limit for the random number
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a valid number next time.")
    quit()

# Generate a random number between 0 and the upper limit
random_number = random.randint(0, top_of_range)
guesses = 0


# Start guessing loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue  # Skip to the next iteration of the loop

    # Check the guess
    if user_guess == random_number:
        print("You got it!")
        break  # Exit the loop when the guess is correct
    else:
        print("You got it wrong! Try again.")
        # Optional: Provide hints
        if user_guess < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
print("You got it in ", guesses, "guesses")