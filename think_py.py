# Exercise 3.1 - Write a function named right_justify that takes a string named 's' as a parameter and 
# prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display

'''def right_justify(s):
    print(" "*(70-len(s))+s)

right_justify('Booby')'''

# Exercise 3.2 - 

'''def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    print(s)
    print(s)

do_twice(print_twice, 'spam')'''

'''import time

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)
                
countdown(5)'''

'''print('Hello World!')
print('What is your name?')
myName = input()
print('It is nice to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')'''


'''while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print(f"Hello, {name}. What is the password? (It is a fish.)")
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')'''

# This is the random number game
'''import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')

    elif guess > secretNumber:
        print('Your guess is too high.')

    else:
        break     # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))'''

'''while True:
    print('Please type your name:')
    name = input()
    if name == "your name":
        break
print("Thank you")'''

'''print('My name is')
for i in range(0, 10, 2):
    print('Jimmy Five Times (' + str(i) + ')')'''

'''def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))'''

import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('************')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()



