'''
A wordle solver - takes (max 5) green and (max 5) yellow letters and prints all possible permutations.
'''

import sys

blanks = "+._-"
results = []
banner = '''
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗██████╗ 
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  ██████╔╝
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   

'''
hlp = f'''
{banner}
Welcome to wordler, a program to help you solve wordle problems.
usage: wordler.py [--green] [--yellow] [--grey] [--help]

--green <args> 	type green letters with wildcards ('+', '.', '_', '-'). Must be 5 characters
--yellow <args> type yellow letters with wildcards ('+', '.', '_', '-'). Must be 5 characters
--grey <args> 	type grey letters (any order, any amount, no wildcards)
--help		prints this help screen


'''

def main():
	green = ""
	yellow=""
	grey=""

	# dictionary = "wordle"

	# if "-d" in sys.argv:
	# 	idx = sys.argv.index("-d")
	# 	try:
	# 		dictionary = sys.argv[idx + 1]
	# 	except IndexError:
	# 		print("-d Requires a dictionary name. Options are: 'wordle' (default), OED")
	# 		return

	if "--green" in sys.argv:
		idx = sys.argv.index("--green")
		try:
			green = sys.argv[idx + 1]
		except IndexError:
			print("--green requires an argument. E.G: 'S--G-'")
			return
	if "--yellow" in sys.argv:
		idx = sys.argv.index("--yellow")
		try:
			yellow = sys.argv[idx + 1]
		except IndexError:
			print("--yellow requires an argument. E.G: 'S--G-'")
			return
	if "--grey" in sys.argv:
		idx = sys.argv.index("--grey")
		try:
			grey = sys.argv[idx + 1]
		except IndexError:
			print("--grey requires an argument. E.G: 'KLXCCRW'")
			return
	if "--help" in sys.argv:
		print(hlp)
		return

	print(banner)
	print("Program will prompt you for green letters (Known letter and position), then yellow (known letter but unknown position), and finally grey (Known not to be in word)")
	print("")
	print("===================================================================================================================================================================")
	print("")


	while len(green) != 5:
		green = input("Input green letters in correct order, using '*'', '/'', '-'' or '&' as blanks. Input should always be 5 characters long:  ").upper().replace(" ", "")
	while len(yellow) != 5:
		yellow = input("Enter yellow letters in correct order, using '*'', '/'', '-'' or '&' as blanks. Input should always be 5 characters long:  ").upper().replace(" ", "")
	
	if not grey:
		grey = input("Enter grey letters in any order. May be more than 5 letters:  ").upper().replace(" ", "")

	with open("wordle") as wordlist:
		for word in wordlist:
			word = word.strip().upper()
			if matches(word, green, yellow, grey):
				results.append(word)
	if results:
		for result in sorted(results):
			print(result)
	else:
		print("No matches found! Make sure you typed your letters correctly and try again.")
		

def matches(word, green, yellow, grey, debug=False):

	for letter in set(grey):
		if green.count(letter) + yellow.count(letter) != word.count(letter):
			if debug:
				print(word, "rejected by GREY rule:", letter)
			return False

	for l, y in enumerate(yellow):
		if word[l] == y: #or y not in word:
			if debug:
				print(word, "rejected by YELLOW position:", y, "at", l)
			return False

		if y not in word and y not in blanks:
			if debug:
				print(word, "rejected by YELLOW missing:", y)
			return False

	for i, g in enumerate(green):
		if word[i] != g and g not in blanks:
			if debug:
				print(word, "rejected by GREEN rule:", g, "at", i)
			return False

	return True


				
if __name__ == "__main__":
	main()