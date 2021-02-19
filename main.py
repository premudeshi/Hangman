import time

print ('hello')

time.sleep(1)

print('start guessing...')
time.sleep(.5)

word = 'chickencurryisgud'

guesses = ''

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)

        else:
            print('_')
            failed += 1

    if failed == 0:
        print('you won')
    break

guess = input('guess a letter: ')
guesses += guess
if guess not in word:
    turns -= -1
    print('wrong')

print('you got', + turns, 'guess some more')

 if turns = 0:
print('you lost bro')