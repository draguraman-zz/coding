def rangeUnion(ranges):
	b = []
	for begin,end in sorted(ranges):
		if b and b[-1][1] >= begin - 1:
			b[-1] = (b[-1][0], end)
		else:
			b.append((begin, end))
	return b

if __name__ == "__main__":
	a = [(7, 9), (11, 13), (11, 15), (14, 20), (23, 39),(67,92),(-1,10)]
	print type(a)
	print rangeUnion(a)
	data = [(1,2,3), (9,5,6), (7,8,9)]

	sorted_default = sorted(data)
	print sorted_default
	sorted_by_second = sorted(data, key=lambda tup: tup[1])
	print sorted_by_second 
