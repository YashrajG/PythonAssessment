import ast
import pprint

# Taking a list of tuples as input directly in the form of python syntax
listOfTuples = ast.literal_eval(input("Enter a list of tuples in python syntax : "))

# Sorting by last element of tuple
listOfTuples.sort(key=lambda x: x[-1])

# pretty printing sorted list to improve readability
pprint.PrettyPrinter().pprint(listOfTuples)

#Output
# Enter a list of tuples in python syntax : [(1,'yash'),(5,'raj'),(2,'yashraj')]
# [(5, 'raj'), (1, 'yash'), (2, 'yashraj')]

