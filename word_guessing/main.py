import random


words = ['name', 'Matrix', 'World', 'Current', 'keyboard']
attempts = 40

random_word = random.randint(0, len(words)-1)
random_word = words[random_word]
random_word = [c.lower() for c in random_word]

players_word = ["-" for c in random_word]


def findNextOccur (s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


while(''.join(players_word) != ''.join(random_word)):
    if attempts == 0:
        print("------------------------")
        print("You have 0 attempts left. You lose the game, try again!")
        print("------------------------")
        break

    print(f"Current word: {''.join(players_word)}")
    print(f'You have {attempts} attempts.')

    guess = input("\nWrite your letter to find out if it is present in the word you are trying to guess: ")[0].lower().strip()

    if not len(guess)-1 == 1:
        print("------------------------")
        print("Please, provide only a single letter!")
        print("------------------------")
        continue

    print(f"Current word: {''.join(players_word)}")

    if guess in random_word:
        print("\n +++++ You guessed a letter! +++++ \n")
        
        occurrences = findNextOccur(random_word, guess)

        for occurrence in occurrences:
            players_word[occurrence] = guess

        if ''.join(players_word) == ''.join(random_word):
            print("------------------------")
            print(f"---- You won a game!, the word was: {''.join(random_word)} ----")
            print("------------------------")

        attempts -= 1
        continue
    else:
        print("\n +++++ Wrong one, try another letter. +++++ \n")
        attempts -= 1
        continue