import random

# Step 1: Create a word bank and randomly select a word
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

# Step 2: Set up placeholders and attempt limit
guessedWord = ['_'] * len(word)
attempts = 10