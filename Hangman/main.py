import random
from art import hangman_art, stages
from words import english, spanish
end_of_the_game=False
lives=7
chosen_word=""
print(hangman_art+"\n")
type=int(input("What language do you want? English type: '1', Spanish type: '2' "))
if type==1:
  numberword=random.randint(0,len(english)-1)#Eligiendo la palabra
  chosen_word=english[numberword].lower()
  print(chosen_word)
elif type==2:
  numberword=random.randint(0,len(spanish)-1)#Eligiendo la palabra
  chosen_word=spanish[numberword].lower()

#print(f"The chosen word is '{chosen_word}'"+"\n")
#creating the display word _ _ _ ...
display_word=[]
for letter in chosen_word:
  display_word+="_"

print(' '.join(display_word)+"\n")
#display=''.join(display_word)
while not end_of_the_game:
  chletter=input("Guess a letter ")
  if chletter in display_word:
    print("You already put that letter in the word")
  chletter=chletter.lower()
  size=len(chosen_word)
  
  
  for i in range (size):# osea de 0 a size-1
    letter=chosen_word[i]
    if letter==chletter:
      display_word[i]=letter
  print("\n"+' '.join(display_word)+"\n")

  if chletter not in chosen_word:
    print(f"Letter '{chletter}' is not in the word you lose a life"+"\n")
    lives-=1
    print(stages[lives]+"\n")
    if lives ==0:
      end_of_the_game=True
      print("You lose")
      print(f"The word was: '{chosen_word}'")
  
  if display_word==list(chosen_word):
    end_of_the_game=True
    print("You Win")
  
  
  




