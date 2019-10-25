'''
NAME:       DANIEL HARKER
ID:         11513968
DATE:       11 Mar 2019
ASSIGNMENT: HW3
PROGRAM:    Windows
'''
from functools import reduce

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1. Dictionaries
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def busStops(b):
    routeDict = {}
    
    #traverse each route in buses
    for route in b:
        #for each stop in the list corresponding to that route
        for stop in b[route]:
            #if stop is not already a key in routeDict, add it and add the route as it's first value
            if stop not in routeDict.keys():
                routeDict[stop] = [route]
            #else, append to rest of routeDict
            else:
                routeDict[stop].append(route)
    
    #now just sort the routeList for each stop
    for stop in routeDict:
        routeDict[stop].sort()
    
    return routeDict
                        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
2. (Dictionaries)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a) addDict(d)
- take dict that has hours studied for each class for each day
- turn it into a dict that tells total hours studied for each class in the week
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def addDict(d):
    hoursPerClass = {}
    
    for day in d:
        for myClass in d[day]:
            if myClass not in hoursPerClass.keys():
                hoursPerClass[myClass] = d[day][myClass]
            else:
                hoursPerClass[myClass] += d[day][myClass]
            
    return hoursPerClass
        
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
b) addDictN(L)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def addDictNHelper(L):
    result = {}
    
    for i in range(len(L)):
        for myClass in L[i]:
            if myClass not in result:
                result[myClass] = L[i][myClass]
            else:
                result[myClass] += L[i][myClass]
                
    return result

           
def addDictN(L): 
    
    result = list(map(addDict, L))
    
    hoursPerClassN = addDictNHelper(result)
    
    return hoursPerClassN

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
3. Dictionaries and lists
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a) searchDicts(L,k)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def searchDicts(L,k):
    myVal = None
    found = False
    L = L[::-1]
    
    #traverse each dic in the reversed list
    for dic in range(len(L)):
        #if the key has been found already, break loop
        if found == True:
            break
        #traverse each key in the current dic
        for key in L[dic]:
            #if current key == desired key, set equal to myVal and set found to True
            if key == k:
                myVal = L[dic][key]
                found = True
    
    return myVal

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
b) searchDicts2(tL,k)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
L2 = [(0,{"x":0,"y":True,"z":"zero"}),
 (0,{"x":1}),
 (1,{"y":False}),
 (1,{"x":3, "z":"three"}),
 (2,{})]

def searchDicts2(tL,k):
    found = False
    myVal = None
    curTuple = tL[-1]

    while found == False:
        curNum = curTuple[0]
        curDict = curTuple[1]
        
        #search tuple's dict for a matching key 
        for key in curDict:
            #if key is found, set myVal to it's value
            if key == k:
                myVal = curDict[key]           
                found = True
        
        #matching key wasn't found in tuple's dict, so set curNum to the num from the tuple
        if found == False:
            curTuple = tL[curNum]
    
    return myVal

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
4. Lists
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
def subsets(L):
    allsubsets = [[]]
      
    def helper(x):
        copy = []
        
        for lst in allsubsets:
            z = lst.copy()
            z.append(x)
            copy.append(z)
        
        for val in copy:
            allsubsets.append(val)                       
            
    for val in L:
        helper(val)
    
    #idea from: https://stackoverflow.com/questions/30346356/how-to-sort-list-of-lists-according-to-length-of-sublists
    allsubsets.sort(key = len)
    
    return allsubsets

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
5. Recursion
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def numPaths(m,n):
    downMoves = 0
    rightMoves = 0
    
    #grid has no moves possible
    if m==0 or n==0:
        return 0
    
    #only 1 possible paths
    if m==1 and n==1:
        return 1
    
    #count number of possible downMoves
    if (m-1)>-1 and n>-1:
        downMoves = numPaths(m-1,n)
    
    #count number of possible rightMoves
    if m>-1 and (n-1)>-1:
        rightMoves = numPaths(m,n-1)
        
    totalMoves = downMoves + rightMoves
    
    return totalMoves

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
6. Iterators
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a) iterPrimes()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def checkIfPrime(x):
    isPrime = True
    
    for i in range(2,x):
        if (x % i) == 0:
            isPrime = False
    
    return isPrime

class iterPrimes():
    def __init__(self):
        self.x = 1
    
    def __next__(self):
        x = self.x
        x+=1
        
        while checkIfPrime(x) == False:
            x+=1
        
        self.x = x
        return x
    
    #used for part 6b
    def __prev__(self):
        x = self.x
        x-=1
        
        while checkIfPrime(x) == False:
            x-=1
        
        self.x = x
        return x

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
b) numbersToSum(iNumbers,summ)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
primes = iterPrimes()

def numbersToSum(iNumbers,summ):
    primesList = []
    curNum = iNumbers.__next__()
    
    #loop while my curNum is less than summ
    #if it's greater than, reached the end of #s to put in
    while curNum < summ:
        primesList.append(curNum)
        summ -= curNum
        curNum = iNumbers.__next__()  
        
        if curNum >= summ:
            iNumbers.__prev__()
            
    return primesList

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
TEST FUNCTIONS
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#1 - busStops
def testbusStops():
    buses = {"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence","Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview","Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
        "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView","Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight","Campus"],
        "Silver": ["TransferStation", "PorchLight", "Stadium","Bishop","Walmart", "Shopco", "RockeyWay"],
        "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand","TacoBell", "Chinook", "Library"],
        "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview","CityHall", "Stadium", "Colorado"]}
    
    if busStops({}) != {}:
        return False
    if busStops(buses) != {'Chinook': ['Blue', 'Lentil', 'Wheat'], 'Orchard': ['Lentil','Wheat'], 'Valley': ['Lentil', 'Wheat'], 'Emerald': ['Lentil'],'Providence': ['Lentil'], 'Stadium': ['Gray', 'Lentil', 'Silver'],
                               'Main': ['Gray', 'Lentil'], 'Arbor': ['Lentil'], 'Sunnyside': ['Gray','Lentil'], 'Fountain': ['Lentil'], 'Crestview': ['Gray', 'Lentil'],
                               'Wheatland': ['Lentil'], 'Walmart': ['Lentil', 'Silver', 'Wheat'],'Bishop': ['Lentil', 'Silver', 'Wheat'], 'Derby': ['Lentil'], 'Dilke':['Lentil'], 'Maple': ['Wheat'], 'Aspen': ['Wheat'], 'TerreView':['Blue', 'Wheat'], 
                               'Clay': ['Wheat'], 'Dismores': ['Wheat'], 'Martin':['Wheat'], 'PorchLight': ['Silver', 'Wheat'], 'Campus': ['Wheat'],
                               'TransferStation': ['Blue', 'Gray', 'Silver'], 'Shopco': ['Silver'],'RockeyWay': ['Silver'], 'State': ['Blue'], 'Larry': ['Blue'], 'Grand':['Blue'], 'TacoBell': ['Blue'], 'Library': ['Blue'], 
                               'Wawawai':['Gray'], 'CityHall': ['Gray'], 'Colorado': ['Gray']}:
        return False
    return True

#2a - addDict
def testaddDict():
    d = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2, '360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    
    if addDict({}) != {}:
        return False
    if addDict(d) != {'355': 8, '360': 9, '451': 8}:
        return False
    return True

#2b - addDictN
def testaddDictN():
    hoursStudiedWeeks = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},'Fri':{'355':2}, 'Sun':{'355':1}},
                     {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},
                     {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},'Sun':{'355':5}}]
    
    if addDictN({}) != {}:
        return False
    if addDictN(hoursStudiedWeeks) != {'355': 16, '360': 24, '451': 6}:
        return False
    return True

#3a - searchDicts
def testsearchDicts():
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

    if searchDicts(L1,"x") != 2:
        return False
    if searchDicts(L1,"y") != False:
        return False
    if searchDicts(L1,"z") != "found":
        return False
    if searchDicts(L1,"t") != None:
        return False
    return True

#3b - searchDicts2
def testsearchDicts2():
    L2 = [(0,{"x":0,"y":True,"z":"zero"}),
          (0,{"x":1}),
          (1,{"y":False}),
          (1,{"x":3, "z":"three"}),
          (2,{})]
    
    if searchDicts2(L2,"x") != 1:
        return False
    if searchDicts2(L2,"y") != False:
        return False
    if searchDicts2(L2,"z") != "zero":
        return False
    return True

#4 - subsets
def testsubsets():
    L3 = [1,2,3]
    
    if subsets([]) != [[]]:
        return False
    if subsets(L3) != [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]:
        return False
    if subsets([(1,"one"),(2,"two")]) != [[],[(1,"one")],[(2,"two")],[(1,"one"),(2,"two")]]:
        return False
    return True

#5 - numPaths
def testnumPaths():
    
    if numPaths(0,5) != 0:
        return False
    if numPaths(1,1) != 1:
        return False
    if numPaths(3,3) != 6:
        return False
    if numPaths(4,5) != 35:
        return False
    return True

#6b - numbersToSum
def testnumbersToSum():
    primes = iterPrimes()
    
    if numbersToSum(primes, 58) != [2, 3, 5, 7, 11, 13]:
        return False
    if numbersToSum(primes, 100) != [17, 19, 23, 29]:
         return False
    return True

#TEST ALL
testFunctions = {"busStops":testbusStops,  "addDict": testaddDict, "addDictN": testaddDictN, "searchDicts": testsearchDicts, "searchDicts2": testsearchDicts2, "subsets":testsubsets, "numPaths": testnumPaths, "numbersToSum":testnumbersToSum  }
if __name__ == '__main__':
    print('---------------------')
    for testName,testFunc in testFunctions.items():
        print(testName,':  ',testFunc())
        print('---------------------')
    
primes = iterPrimes()
primes.__next__()
primes.__next__()
primes.__next__()

primes = iterPrimes()
print(numbersToSum(primes,58))
print(numbersToSum(primes,100))