'''
A wordle solver - takes (max 5) green and (max ?) yellow letters and prints all possible permutations.

0. find wordlists.
0.5. ability to choose wordlists (wordle, scrabble, OED...)
1. take and sanitise a user input. loop until acceptable (with error message(s))
1.5 take command line args
2.
'''

import sys

blanks = "*/.@&_-"
results = []

def main():
	# if len(sys.argv) > 1:
	# 	args = sys.argv[1:]
	# 	if --help in args:
	# 		...
	# 	elif 
	# 		...
	#else:
		print("Program will prompt you for green letters (Known letter and position), then yellow (known letter but unknown position), and finally grey (Known not to be in word)")
		print("===================================================================================================================================================================")
		green = input("Input green letters in correct order, using '*'', '/'', '-'' or '&' as blanks. Input should always be 5 characters long:  ").upper().replace(" ", "")
		yellow = input("Enter yellow letters in any order. Should be no more than 5 letters:  ").upper().replace(" ", "")
		grey = input("Enter grey letters in any order. May be more than 5 letters:  ").upper().replace(" ", "")

	with open("wordle-wordlist") as wordlist:
		for word in wordlist:
'''
For each letter:

Minimum count
= number of times it appears as green + yellow

Maximum count

If the letter ever appears as grey,
then max count = minimum count

Otherwise, max count is unbounded

A candidate word is valid only if its count for that letter falls within those bounds.
'''

def matches(word, green, yellow, grey):
	'''for j, gr in enumerate(grey):
		if word[j] == gr and gr not in blanks:
			return False'''
	for letter in set(grey):
		if green.count(letter) + yellow.count(letter) > word.count(letter):
			return False

	for l, y in enumerate(yellow):
		if word[l] == y or y not in word:
			return False

	for letter in set(yellow):  
		if green.count(letter) + yellow.count(letter) > word.count(letter):
			return False

	for i, g in enumerate(green):
		if word[i] != g and g not in blanks:
			return False

	return True
				
if __name__ == "__main__":
	main()