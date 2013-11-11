from collections import defaultdict
from sys import argv
import collections


def  IsIsoMorphic(a,b):
    dictA = dictB = defaultdict(str)
    for i,c in enumerate(a):
        dictA[c] = i
        dictB[b[i]] = i
    return encode(b,dictB) == encode(a,dictA)

def encode(a,dic):
    return ''.join(str(dic[c]) for c in a)

if __name__ == "__main__":
	name,n1,n2=argv
	print IsIsoMorphic(n1,n2)
