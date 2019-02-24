#!/usr/bin/env python3

word = []

length = int(input('How many letters in your word? '))

while len(word) < length:
  letter = input('Enter a letter: ')
  word.append(letter.strip()[:1])

print(word)
