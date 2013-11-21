from sys import argv
from collections import Counter
def longestUniqueWord(str):
	c=Counter()
	d=defaultDict()
	words=str.split()
	wordWithMaxLength=""
	for word in words:
		c[word]+=1
		if(c[word] == 1 and  len(word)>len(wordWithMaxLength) ):
			wordWithMaxLength=word
	return wordWithMaxLength


if __name__ == "__main__":
	name,arg1=argv
	print longestUniqueWord(arg1)

#with open('paper.txt', 'r') as file:
    #for line in file:
#for i,c in enumerate(new_str):
		#print i,c