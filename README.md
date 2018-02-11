# Suffix Tree -

A Suffix Tree for a given text is a compressed trie for all suffixes of the given text.

# Generalised Suffix Tree -

A generalised suffix tree is a compressed trie that contains all the suffixes of more than one text. 


# About Repository -

This repository contains python implementation of suffix tree. It also includes code to
showcase various applications where suffix trees are used. The applications include -

	1) searching for a query string in a text.
	
	2) searching for the longest substring of a string in a text.

	3) ranking various texts according to relevance with respect to a particular string.

There are many ways of constructing a suffix tree. The one I am using is called 
McCreight’s algorithm and its time complexity is O(m^2) where m is the length 
of the string for which we want to construct the suffix tree.
