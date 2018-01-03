# this file is used for preprocessing an input file (Here we are trying to preprocess 'AesopTales.txt' file)


# this function creates a list containing the titles of all the tales, in the order in which they appear in ‘ AesopTales.txt’ file
# this function also converts each story into a string and appends them into a list
def extract(x,z) :

	# here x is the file we want to preprocess
	# z is the list which will eventually contain the titles of all the tales 
	y = ""
	file = open(x, 'r')
	l = []
	for ch in file :
		a = ch.split(" ")
		l.append(a)

	content = []
	count = 0
	
	for i in range(0,len(l)):
		if i==0:
			z.append(l[i])

		# I am appending a '$' at the end of every story
		elif (l[i-2]==['', '\n'] or l[i-2]==['\n']) and (l[i-1]==['\n'] or l[i-1]==['','\n']) and (l[i] != ['\n']) and (l[i] != ['','\n']) and (len(l[i])<11):
			m = "$" + " "
			count = count + 1
			content.append([m])
			z.append(l[i])
	
		else :
			content.append(l[i])

	content.append(["$" + " "])

	# here I am appending all the titles into z 
	for i in range(0,len(z)):
		s1 = ""
		for j in range(0,len(z[i])-2):
			s1 = s1+z[i][j]+" "
		s1 = s1+z[i][len(z[i])-2]
		z[i] = s1

	# here I am creating a single string by appending all the stories (each having a '$' at the end)
	for k in range(0,len(content)):
		t = ""
		if content[k]!=['\n'] and content[k]!=['','\n'] :
			length = len(content[k])
		
			if length == 1 :
				if content[k][0][len(content[k][0])-1] != '\n' :
					t = t + content[k][0]
				else :
					t = t + content[k][0][0:len(content[k][0])-1] + " "

			else :
				for m in range(0,length-1) :
					t = t + content[k][m] + " "	
				for n in range(0,len(content[k][length-1])-1) :
					t = t + content[k][length-1][n]
				t = t + " "
	
		y = y + t

	# here I am creating a list which titles of tales as its elements
	output = y.split('$')
	for i in range(0,len(output)) :
		output[i] += '$' + str(i) # here we are trying to append '$'+string(index of the tale) at the end of every tale
	return output



# this function removes the stopwords from a text string
def remove_stopwords(a):
	
	# a is a list containing input strings
	# here I am creating a list of stopwords
	stopwords = ['ourselves','He','I','She','The','You','Then', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 'being', 'if','If', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than','thus','It','A','upon','They','will','would','shall','should','ever','never','able']

	val3 = []

	for i in range(0,len(a)):
		val2 = ""

		# here I am removing punctuations
		for j in range(0,len(a[i])):
			if a[i][j]!='\"' and a[i][j]!=',' and a[i][j]!='.' and a[i][j]!=':' and a[i][j]!='!' and a[i][j]!=';':
				val2 += a[i][j]

		l = val2.split(" ")
		l1 = []
	
		for i in range(0,len(l)):
			if l[i]!='':
				l1.append(l[i])

		l2 = []

		# here I am removing the stopwords
		for k in l1:
			if k not in stopwords:
				l2.append(k)

		out = ""
		for i in range(0,len(l2)-1):
			out = out + l2[i] + " "
		out = out + l2[len(l2)-1]
	
		val3.append(out)

	# here we are returning the list of strings, where no string has any stopwords present in it
	return(val3)

