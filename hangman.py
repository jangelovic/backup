# hangman game
import random

print("Welcome to hangman guess the right word before it's to late :) ")

myWord = ("Yeet", "Reet", "Bruh", "Potato", "Buddy")

word = random.choice(myWord)

choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else:
	print("Not a match")

letter = input("Type a letter")
if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")

count = 0
for s in myWord:
	if s == letter:
		print(count)
	count += 1


