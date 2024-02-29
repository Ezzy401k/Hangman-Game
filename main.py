import random
import warnings
warnings.filterwarnings("ignore")
import art
import words_list
word_list = words_list.word_list
stages = art.stages
chosen_word = list(random.choice(word_list))
print(f"chosen word is : {chosen_word}")
print(art.logo)
display = []
life = 6
for letter in chosen_word:
    display += "_"

priveous = []

while not display == chosen_word:
    guess = input("Guess a letter: ").lower()
    if guess not in priveous:
      for i in range(0,len(chosen_word)):
          if chosen_word[i] == guess:
              display[i] = guess
      
      if guess not in chosen_word:
          life -= 1
          print(f"You guessed {guess}, Thats not in the word. You lose a life.")
          
          if life == 0:
              print(stages[life])
              print("You Lose!")
              break
      

      print(f"{' '.join(display)}")
      
      if display == chosen_word:
          print("You Win!")
    else:
        print(f"You have already guessed {list(set(priveous))}")
    priveous += guess
    print(stages[life])
