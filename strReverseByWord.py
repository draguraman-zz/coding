from sys import argv
def strReverseByWord(string):
	words=string.split()
	new_str=""
	for word in words:
		new_str=new_str+word[::-1]+" "
	print new_str	
	for i,c in enumerate(new_str):
		print i,c
if __name__ == "__main__":
	name,arg1=argv
	strReverseByWord(arg1)

