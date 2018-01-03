import suffix_tree as stree
import preprocess as r

# this function returns a list containing all the substrings of an input string
def get_all_substrings(a):
	sub = []
	length = len(a)

	for i in range(0,length+1):
		for j in range(0,length-i):
			sub.append(a[j:j+i+1])
	
	return(sub)


# this function is used to print a sentence containing a particular query string
def occurences(a,b,c):
	for i in range(1,len(a)):
		wow = a[i]

		if wow-10>=0 and wow+len(c)+10<=len(b[a[0]]):
			j = wow

			while(j>=0)and(b[a[0]][j] != '.')and(b[a[0]][j] != '$'):
				j -= 1

			k = wow+len(c)

			while(k<len(b[a[0]]))and(b[a[0]][k] != '.')and(b[a[0]][k] != '$'):
				k += 1

			print(b[a[0]][j+1:k+1],"\n")

		elif wow-10<0:
			k = wow+len(c)

			while(k<len(b[a[0]]))and(b[a[0]][k] != '.')and(b[a[0]][k] != '$'):
				k += 1

			print(b[a[0]][0:k+1],"\n")

		else:
			j = wow

			while(j>=0)and(b[a[0]][j] != '.')and(b[a[0]][j] != '$'):
				j -= 1

			print(b[a[0]][j+1:],"\n")


# this function solves the first sub-problem
def first_problem(a,b,c):
	tree = stree.Suffix_tree()

	for i in range(0,len(b)):
		tree.add(b[i])

	out = tree.search(a)

	if out!=-1:
		out.sort()	
		k = 0
		out2 = []

		while k<len(out):
			out3 = [out[k][0],out[k][1]]
			j = 1

			while k+j<len(out) and out[k][0]==out[k+j][0]:
				out3.append(out[k+j][1])
				j += 1

			out2.append(out3)
			k += j

		for i in range(0,len(out2)):
			if out2[i][0]<len(c):
				print("\t\t\t\tTITLE OF THE TALE WHERE THE QUERY STRING '",a,"' WAS FOUND => \n")
				print("\t\t\t\t\t\t'",c[out2[i][0]],"'\n\n\n")
				print("\t\t\tSENTENCES WHERE THE QUERY STRING '",a,"' HAS OCCURED IN THE ABOVE TALE ARE => \n")
				occurences(out2[i],b,a)
				print("\n")
				print("------------------------------------------------------------------------------------------------------------------------------------")
				print("\n")

	else:
		print("\n\n\t\tTHE GIVEN QUERY STRING '",a,"' WAS NOT FOUND ANYWHERE IN THE TEXT\n")
		print("------------------------------------------------------------------------------------------------------------------------------------------")


# this function solves the second sub-problem
def second_problem(a,b,c):
	tree = stree.Suffix_tree()

	for i in range(0,len(b)):
		tree.add(b[i])

	out = tree.search(a)

	found = [[0,0,0]]*len(c)

	if out!=-1:
		out.sort()
		k = 0
		out2 = []

		while k<len(out):
			out3 = [out[k][0],out[k][1]]
			j = 1

			while k+j<len(out) and out[k][0]==out[k+j][0]:
				out3.append(out[k+j][1])
				j += 1

			out2.append(out3)
			k += j

		for i in out2:
			found[i[0]] = [i[1],1,a]


	subs = get_all_substrings(a)
	i = len(subs)-2

	while i>=0:
		out = tree.search(subs[i])
		
		if out!=-1:
			out.sort()
			k = 0
			out2 = []

			while k<len(out):
				out3 = [out[k][0],out[k][1]]
				j = 1

				while k+j<len(out) and out[k][0]==out[k+j][0]:
					out3.append(out[k+j][1])
					j += 1

				out2.append(out3)
				k += j

			for j in out2:
				if j[0]<len(found) and found[j[0]][0] == 0:
					found[j[0]] = [j[1],0,subs[i]]
					
		i -= 1

	for k in range(0,len(found)):
		if found[k][0]==0:
			print("\n\n\t\tTHE GIVEN QUERY STRING '",a,"' & ITS SUBSTRINGS WERE NOT FOUND ANYWHERE IN THE TALE WHOSE TITLE IS =>\n")
			print("\t\t\t\t\t'",c[k],"'\n\n\n")
			print("------------------------------------------------------------------------------------------------------------------------------------------")
	
		else:
			if found[k][1]==1:
				print("\n\n\t\tTITLE OF THE TALE WHERE THE QUERY STRING '",a,"' WAS FOUND IN THE TEXT => \n")
				print("\t\t\t\t'",c[k],"'\n\n\n")
				print("\n\t\t\tSENTENCE WHERE THE QUERY STRING '",a,"' FIRST OCCURED IN THE ABOVE TALE => \n\n")
				occurences([k,found[k][0]],b,a)
				print("------------------------------------------------------------------------------------------------------------------------------------------")
	
			else:
				print("\n\n\tTITLE OF THE TALE WHERE THE SUBSTRING '",found[k][2],"' OF THE QUERY STRING '",a,"' WAS FOUND IN THE TEXT => \n")
				print("\t\t\t\t\t'",c[k],"'\n\n")
				print("\n\t\tSENTENCE WHERE THE SUBSTRING '",found[k][2],"' OF THE QUERY STRING '",a,"' FIRST OCCURED IN THE ABOVE TALE => \n\n")
				occurences([k,found[k][0]],b,found[k][2])
				print("------------------------------------------------------------------------------------------------------------------------------------------")

		

# this function solves the third sub-problem
def third_problem(a,b,c):
	tree = stree.Suffix_tree()

	for i in range(0,len(b)):
		tree.add(b[i])

	rank = [0]*len(c)
	count = 1
	out = tree.search(a)
	
	if out!=-1:
		out.sort()
		k = 0
		out2 = []

		while k<len(out):
			out3 = [0,out[k][0]]
			j = 1

			while k+j<len(out) and out[k][0]==out[k+j][0]:
				j += 1
		
			out3[0] += j
			out2.append(out3)
			k += j
		
		out2.sort()
		out2.reverse()
		for j in range(0,len(out2)):
			rank[out2[j][1]] = count
			count += 1

	if 0 in rank:
		d = (r.remove_stopwords([a]))[0].split(" ")
		outing = [[0,0]]*len(rank)
		for j in range(0,len(outing)):
			outing[j] = [0,j]


		for i in d:
			out4 = tree.search(i)
			if out4!=-1:
				for j in range(0,len(out4)):
					if out4[j][0]<len(outing):
							outing[out4[j][0]][0] += 1
			
		outing.sort()
		outing.reverse()
				
		k = 0
		while k<len(outing) and outing[k][0] != 0:
			if rank[outing[k][1]] == 0:
				rank[outing[k][1]] = count
				count += 1
			k += 1

	if 0 in rank:
		subs2 = get_all_substrings(a)
		i = len(subs2)-2

		outing = [[0,0]]*len(rank)

		for j in range(0,len(outing)):
			outing[j] = [0,j]

		while i>=0:
			output = tree.search(subs2[i])
			if output!=-1:
				for j in range(0,len(output)):
					if output[j][0]<len(outing):
						outing[output[j][0]][0] += len(subs2[i])
			i -= 1
			
		outing.sort()
		outing.reverse()
				
		k = 0
		while k<len(outing) and outing[k][0] != 0:
			if rank[outing[k][1]] == 0:
				rank[outing[k][1]] = count
				count += 1
			k += 1
		
	if 0 in rank:	
		for q in range(0,len(rank)):
			if rank[q]==0:
				rank[q]=count
	
	last_out = [[0,0]]*len(c)

	for j in range(0,len(rank)):
		last_out[j] = [rank[j],j]

	last_out.sort()
	print("\t\tTITLES OF THE TALES IN ORDER OF RELEVANCE (FROM HIGHEST TO LOWEST) FOR THE QUERY STRING '",a,"' ARE =>\n\n")
	for i in last_out:
		print("\t\t\t\t'",c[i[1]],"'\n")
	
