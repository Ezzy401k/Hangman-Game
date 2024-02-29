import random
import warnings
warnings.filterwarnings("ignore")
# import custom modules.
import art
import words_list
word_list = words_list.word_list
stages = art.stages

# select a random word from the list.
chosen_word = list(random.choice(word_list))

# This line of code displays the selected word hide it when using the code "used for debugging".
print(f"chosen word is : {chosen_word}")

print(art.logo)
# create an empty list.
display = []

life = 6
# insert _ for every letter in the chosen word to the new list.
for letter in chosen_word:
    display += "_"
# create a new list.
priveous = []
# make a loop.
while not display == chosen_word:
    # acceot the user's input.
    guess = input("Guess a letter: ").lower()
    # if guess is not in previeous do this.
    if guess not in priveous:
      for i in range(0,len(chosen_word)):
          # if the chosen word and the guessed letter are the same replace the letter in the display position with the guess letter.
          if chosen_word[i] == guess:
              display[i] = guess
      # if guess is not in the chosen word decrease one life.
      if guess not in chosen_word:
          life -= 1
          print(f"You guessed {guess}, Thats not in the word. You lose a life.")
          # if the user loses all life end the game.
          if life == 0:
              print(stages[life])
              print("You Lose!")
              break
      
        # show the letters together.
      print(f"{' '.join(display)}")
      # if the final word and the chosen word are the same your win will be displayed.
      if display == chosen_word:
          print("You Win!")

    # If the user inputs the same letter show this text.
    else:
        print(f"You have already guessed {list(set(priveous))}")
    # Add the new inputted letter to the list.
    priveous += guess
    # shows how many lives are left.
    print(stages[life])
input("Tap Enter to EXIT!")
