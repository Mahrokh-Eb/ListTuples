# makoing list, tuple, dictionary
firstList = [6, 9, 20, 9999, 11, 50]
print(firstList)

firstTuple = (6, 6, 6, 8, 89, 12, 76)
print(firstTuple)

firstDict = {'age': 33, 'name': 'Sara', 'major': "computerScience"}
print(firstDict)

# using functions for List
x = firstList.count(11)
print(x)

y = firstList.index(11)
print(y)

firstList.append(66)
print(firstList)

firstList.append(888)
print(firstList)

firstList.pop()
print(firstList)

firstList.sort()
print(firstList)

# using functions for Tuple
z = firstTuple.count(6)
print(z)

t = firstTuple.index(76)
print(t)

# using functions for dictionary
print(firstDict.items())
print(firstDict)
print(firstDict.get('age'))
print(firstDict['name'])

