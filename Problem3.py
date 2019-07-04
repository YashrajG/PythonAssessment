import functools
import ast

listOfStrings = ast.literal_eval(input("Enter a list of strings in python format : "))
lexList = ast.literal_eval(input("Enter the lexical order of alphabets as a list of strings in python format : "))

def compareStrings(s1, s2):
	l = len(s1) if len(s1) < len(s2) else len(s2)
	for i in range(l):
		if s1[i] != s2[i]:
			return lexList.index(s1[i]) - lexList.index(s2[i])

	return len(s1) - len(s2)

listOfStrings.sort(key=functools.cmp_to_key(compareStrings))

print(listOfStrings)