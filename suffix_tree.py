# this function finds the number of corresponding character matches of 2 strings
def num_match(a,b):
	length = len(a)
	suffix_length = len(b)
	count = 0

	if(length >= suffix_length):
		if(a[0]==b[0]):
			for i in range(0,suffix_length):
				if(a[i] == b[i]):
					count +=1

				else:
					break

	else:
		if(a[0]==b[0]):
			for i in range(0,length):
				if(a[i] == b[i]):
					count +=1

				else:
					break

	return count



# this class represents a suffix tree
class Suffix_tree(object):

	def __init__(self):
		self.root = Node(None,None) #initialising a root node
	
	
	# this function is used to add all the suffixes of a string into the suffix tree
	def add(self,word): 
		new_word = word
		suffixes = [new_word[i:] for i in range(0,new_word.index('$'))]

		for i in range(0,len(suffixes)):
			self.suffix_insert(self.root,suffixes[i],i)

	
	# this function is used to insert a suffix into the suffix tree
	def suffix_insert(self,node,suffix,number):
		child = node.get_children(suffix[0])
	
		if(child == None): # if no child exists whose substring begins with the same character as of the string to be inserted
			newChild = Node(suffix,number)
			node.set_children(suffix,newChild)
			return
		
		# if the string to be inputed is already present in the suffix tree
		if(child.children == {}) and (child.substring == suffix):
			return

		num_matched = num_match(child.substring, suffix)
		

		if(num_matched==len(child.substring) and (child.children!={})):
			self.suffix_insert(child,suffix[num_matched:],number)
			return
		
		elif(len(child.substring) < len(suffix)):
			if(child.children == {}):
				new_child_string = child.substring[:num_matched]

				if(child.substring != new_child_string):
					node.children[new_child_string] = node.children[child.substring]
					del node.children[child.substring]

				if(len(child.substring)>1 and len(child.substring)!=num_matched):
					rest_child_string = child.substring[num_matched:]
					new_internal_node = Node(rest_child_string,child.suffixnum)
					
					for child_string,child_node in child.children.items():
						new_internal_node.set_children(child_string,child_node)
					
					child.children.clear()
					child.set_children(rest_child_string,new_internal_node)
					
				child.substring = new_child_string
				self.suffix_insert(child,suffix[num_matched :],number)	
				return
	
		
		new_internal_node = Node(suffix[:num_matched],child.suffixnum)
		del node.children[child.substring]

		new_child_node = Node(suffix[num_matched:],number)
		child.substring = child.substring[num_matched:]

		new_internal_node.set_children(suffix[num_matched:],new_child_node)
		new_internal_node.set_children(child.substring,child)

		node.set_children(suffix[:num_matched],new_internal_node)
		return

	
	# finds the number present after '$' which will be later used for indexing
	def find_tale(self,node,s,num):
		if s!="":
			num.append([int(s),node.suffixnum])

		if node.children!={}:
			for j in node.children:
				self.find_tale(node.children[j],j+s,num)

		return(num)

	
	# if we find a match for the query string then this function is used to find the '$' symbol		
	def find_dollar(self,node):
		index = node.substring.find('$')

		if index==-1:
			li = []
			for j in node.children:
				val = self.find_dollar(node.children[j])
				for k in range(0,len(val)):
					li.append(val[k])

			return(li)

		else:
			l = []
			s = ""
			num = []
			s += node.substring[index+1:]
			out = self.find_tale(node,s,num)

			for j in range(0,len(out)):
				l.append(out[j])

			return(l)


	# this function is used to find a match for the given query string
	def find(self,node,s):
		child = node.get_children(s[0])
		
		if child==None:
			return(-1)

		else:
			num_matched = num_match(s,child.substring)
			
			if len(child.substring)==len(s):
				if num_matched==len(child.substring):
					return(self.find_dollar(child))
				
				else:
					return(-1)

			elif len(s)<len(child.substring):
				if num_matched==len(s):
					return(self.find_dollar(child))
				
				else:
					return(-1)

			else:
				if num_matched==len(child.substring):
					return(self.find(child,s[num_matched:]))
				
				else:
					return(-1)				


	def search(self,s):
		return(self.find(self.root,s))
		


# This class represents a Node in the suffix tree
class Node(object):

	def __init__(self,substring,suffixnum):
		self.children = {} # dictionary having key as the substring that led to that child and value as the child node
		self.suffixnum = suffixnum # suffix no.
		self.substring = substring # the one which led to this node


	# is used to find a child whose key startswith a particular character
	def get_children(self,firstChar):
		child = firstChar
		keys = list(self.children.keys())

		if(keys != []):
			for key in keys:
				if(key.startswith(child)):
					return self.children[key]

		else:
			return None

	# is used to enter a new key,value pair into the children dictionary
	def set_children(self,substring,child):
		self.children[substring] = child


