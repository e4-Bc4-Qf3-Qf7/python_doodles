#!/usr/bin/env python3

hangman = 0
word = []
guessed = []

length = int(input('How many letters in your word? '))
while len(word) < length:
  letter = input('Enter a letter: ')
  word.append(letter.strip()[:1])
while hangman == 0:
  inputResponse01 = (input("Guess a letter"))
  if inputResponse01 in word :
    print ("correct")
  elif inputResponse01 in guessed:
    print ("You have already guessed that letter")
  else:
    print ("That is not the correct letter")
    word.append(guessed.strip()[:1])
  if guessed == 5 :
    hangman = 1
  if len(word) == 0:
    hangman = -1