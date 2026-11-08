import random

# Step 1: Create a word bank and randomly select a word
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

# Step 2: Set up placeholders and attempt limit
guessedWord = ['_'] * len(word)
attempts = 10
# Step 3: Main Game Loop
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
# Win condition: no underscores left
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
# Loss condition: ran out of attempts
if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
