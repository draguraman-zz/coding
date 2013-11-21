def binarySearch(a,val):
	if len(a)==1 and val == a[0] :
		return True
	elif (len(a)==1 and not (val == a[0]) ):
		return False
	else:
		i=len(a)/2
		if (val>a[i]):
			binarySearch(a[i:],val)
		else:
			binarySearch(a[:i],val)

def pivotedSearch(val):
	a=[7,8,1,2,3,4,5,6]
	#find point of pivot
	prev=a[0]
	for index,i in enumerate(a):
		print index,i
		if i<prev:
			pivot_index=index-1
			print pivot_index
			break
		else:
			prev=i
	print pivot_index
	a1=a[:pivot_index+1]
	print a1
	a2=a[pivot_index+1:]
	print a2
	if val < a1[0]:
		flag=binarySearch(a1,val)
	else:
		flag=binarySearch(a2,val)
	print flag
if __name__ == "__main__" :
	pivotedSearch(5)

