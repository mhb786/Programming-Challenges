print('Guess a 6-digit number SLAYER so that the following equation is true, where each one stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS')
guess = str(input('Enter your guess for SLAYER: '))

def answer(guess):
    return int(guess) * 3

answer = answer(guess)

def layers(guess):
    return str(guess[1:7]) + str(guess[0])

layers = int(layers(guess))

if answer == layers:
    print('Your guess is correct: ')
else:
    print('Your guess is incorrect: ')

print(f'SLAYER + SLAYER + SLAYER = {answer} \nLAYERS = {layers} \nThanks for playing')