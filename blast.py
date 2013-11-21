import itertools
with open("./fp/1kb_id_131.fa", mode="r") as file:
	reader = file.read()
	paralog_set=set()
	for i,part in enumerate(reader.split(">")):
		part=">"+str(part)
		paralog_set.add(part)
	#print paralog_set
	cartesian_product=set()
	cartesian_product=set(itertools.product(paralog_set,repeat=2))
	f1=open('out.txt', 'w+')
	for i in cartesian_product:
		f1.write(str(i)+"\n")
	#for i,j in cartesian_product:


		
