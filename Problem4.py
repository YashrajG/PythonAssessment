import ast

pairSetList = ast.literal_eval(input("Enter the pairs of employees in the format [{e1,e2},{e3,e4},...] : "))
groupSetList = [ pairSetList.pop(0) ]

for employeePair in pairSetList:
	for groupNo,group in enumerate(groupSetList):
		if(type(group) == type('')):
			break
		if len(employeePair.intersection(group)) > 0 :
			groupSetList[groupNo] = group.union(employeePair)

			for groupNo2,group2 in enumerate(groupSetList):
				if len(group2.intersection(group)) > 0 and groupNo2 != groupNo:
	
					groupSetList[groupNo] = groupSetList[groupNo].union(group2)
					groupSetList.pop(groupNo2)
					break
			break
		else :
			groupSetList.append(employeePair)

print("Number of groups = " + str(len(groupSetList)) )

inputPair = ast.literal_eval(input("Enter a pair of employees in the format [e1,e2] : "))

isConnected = False
for groupSet in groupSetList:
	if inputPair[0] in groupSetList and inputPair[1] in groupSetList:
		isConnected = True

print("They are " + "" if isConnected else "not " + "connected.")