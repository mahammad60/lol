#secret word is dragon
secret_word = "dragon"
#variable is guess and stores input with it
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not (out_of_guesses):
 if guess_count < guess_limit:
  guess = input(" guess the word ")
  guess_count += 1
 else:
  out_of_gueses= True
  if out_of_guesses:
   print("out of guessess")
  else:
     print("you win")















