newlist = []

with open("wordle-wordlist", 'r') as file:
	for line in file:
		newlist.append(line.partition("	")[0])

with open("wordlist2.txt", 'a') as file:
	for x in newlist:
		file.write(x + "\n")


print(newlist[0])