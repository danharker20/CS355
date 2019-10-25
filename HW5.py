'''
NAME:       DANIEL HARKER
ID:         11513968
DATE:       3 Apr 2019
ASSIGNMENT: HW5
PROGRAM:    Windows
'''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
OPERAND STACK
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
opstack = []  #assuming top of the stack is the end of the list

'''pop last value from opstack'''
def opPop():
    
    '''return last val in opstack'''
    if len(opstack) > 0:
        return opstack.pop((len(opstack)) - 1)
    
    else:
        print("opPop(): Not enough values in opstack")

'''push value to end of opstack'''
def opPush(value):
    
    opstack.append(value)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DICTIONARY STACK
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
dictstack = []  #assuming top of the stack is the end of the list

'''pop last value from dictstack'''
def dictPop():
    
    if len(dictstack) > 0:
        return dictstack.pop((len(dictstack)) - 1)
    
    else:
        print("dictPop(): Not enough values in dictstack")

'''push value to end of dictstack'''
def dictPush(d):
    
    dictstack.append(d)

'''add name:value to top dict in dictstack'''
def define(name, value):
    
    '''if not empty, add name:value pair to top dict'''
    '''else, create a new dict and push it to dictstack via dictPush'''
    if len(dictstack) > 0:
        (dictstack[-1][1])[name] = value
        
    else:
        newDict = {}
        newDict[name] = value
        dictPush((0, newDict))

'''looks up name in dicionaries of dictstack. if found, return the value'''
def lookup(name, scope):
    fullName = '/' + name    
    
    if scope == 'dynamic':           #dynamic - search for most recent declaration
        revdictstack = reversed(dictstack)
        
        for level in revdictstack:  #traverse dictstack from top to bottom
            (index, dic) = level

            if fullName in dic:
                return (index, dic[fullName])
            
        return None
        
    elif scope == 'static':
        index = len(dictstack) - 1
        dic = list(dictstack)

        return findStaticLink(index, dic, fullName)

'''add for HW5'''
def findStaticLink(curIndex, dic, curName):
    
    if curName in dictstack[curIndex][1]:
        return (curIndex, dictstack[curIndex][1][curName])

    elif curIndex == dictstack[curIndex][0]:
        return None

    else:
        (newIndex, pop) = dictstack[curIndex]
        pop = dic.pop(curIndex)
        return findStaticLink(newIndex, dic, curName)
    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ARITHMETIC AND COMPARISON OPERATORS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''add'''
def add():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''make sure both values are numbers (int or float) - learned from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not'''
        if (isinstance(val1, int) or isinstance(val1, float)) and (isinstance(val2,int) or isinstance(val2,float)):
            opPush(val2 + val1)
            
        else:
            print("add(): both values are not int/float")
    
    else:
        print("add(): not enough values in opstack")

'''sub'''
def sub():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''make sure both values are numbers (int or float) - learned from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not'''
        if (isinstance(val1, int) or isinstance(val1, float)) and (isinstance(val2,int) or isinstance(val2,float)):
            opPush(val2 - val1)
            
        else:
            print("sub(): both values are not int/float")
    
    else:
        print("sub(): not enough values in opstack")

'''mul'''
def mul():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''make sure both values are numbers (int or float) - learned from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not'''
        if (isinstance(val1, int) or isinstance(val1, float)) and (isinstance(val2,int) or isinstance(val2,float)):
            opPush(val2 * val1)
            
        else:
            print("mul(): both values are not int/float")
    
    else:
        print("mul(): not enough values in opstack")

'''div'''
def div():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''make sure both values are numbers (int or float) - learned from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not'''
        if (isinstance(val1, int) or isinstance(val1, float)) and (isinstance(val2,int) or isinstance(val2,float)):
            opPush(val2 / val1)
            
        else:
            print("div(): both values are not int/float")
    
    else:
        print("div(): not enough values in opstack")

'''mod'''
def mod():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''make sure both values are numbers (int or float) - learned from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not'''
        if (isinstance(val1, int) or isinstance(val1, float)) and (isinstance(val2,int) or isinstance(val2,float)):
            opPush(val2 % val1)
            
        else:
            print("mod(): both values are not int/float")
    
    else:
        print("mod(): not enough values in opstack")

'''check for equality'''
def eq():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''checking for equality'''         
        if val2 == val1:
            areEqual = True
            
        else:
            areEqual = False
            
        opPush(areEqual)

    else:
        print("eq(): not enough values in opstack")

'''less than'''       
def lt():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''checking for less than'''
        if val2 < val1:
            isLT = True
        else:
            isLT = False
        
        opPush(isLT)
    
    else:
        print("lt(): not enough values in opstack")

'''greater than'''
def gt():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        
        '''checking for greater than'''
        if val2 > val1:
            isGT = True
        else:
            isGT = False
        
        opPush(isGT)
    
    else:
        print("gt(): not enough values in opstack")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
STRING OPERATORS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''length of first val of opstack'''
def length():
    
    if len(opstack) > 0:
        val = opPop()
        lenVal = 0
        
        ''' make sure it doesn't count parenthesis'''
        for char in val:
            if char != '(' and char != ')':
                lenVal += 1
                
        opPush(lenVal)
    
    else:
        print("length(): not enough values in opstack")

'''get str[index] by popping index, then popping str'''
def get():
    
    if len(opstack) > 1:
        index = opPop()
        string = opPop()
        
        '''remove parenthesis from string'''
        if string[0] == '(':
            string = string[1:]
        if string[len(string) - 1] == ')':
            string = string[:(len(string)) - 1]
        
        '''check for valid index'''
        if index < len(string):
            opPush(ord(string[index]))
        
        else:
            print("get(): index is too big")
            
    else:
        print("get(): not enough values in opstack")

'''gets string, index, count from stack; returns substring of string from index to count'''
def getinterval():
    
    if len(opstack) > 2:
        count = opPop()
        index = opPop()
        string = opPop()
        
        '''remove parenthesis from string'''
        if string[0] == '(':
            string = string[1:]
        if string[len(string) - 1] == ')':
            string = string[:(len(string)) - 1]

        '''get the string and put it in parenthesis'''
        string = '(' + string[index:(index+count)] + ')'
        
        opPush(string)
    
    else:
        print("getinterval(): not enough values in opstack")

'''gets string, index, ASCII val from stack; replaces char at index with new char in string'''
def put():
    
    if len(opstack) > 3:
        asciiVal = opPop()
        index = opPop()
        string = opPop()
        
        ''' make a copy of opstack '''
        tempstack = []
        
        for item in opstack:
            tempstack.append(item)
                
        ''' clear opstack - so I can then push items regardless of changed/not '''
        clear()
        
        ''' if there's a duplicate, change it and opPush OR just opPush '''
        for item in tempstack:
            if item == string:
                if item[0] == '(':
                    item = item[1 : (len(item) - 1)]
                    
                    strToList = list(item)
                    strToList[index] = chr(asciiVal)
                    item = "".join(strToList)
                    opPush('(' + item + ')')
            
            else:
                opPush(item)
            
    else:
        print("put(): not enough values in opstack")    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
STACK MANIPULATION AND PRINT OPERATORS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''duplicate top value on stack'''
def dup():
    
    if len(opstack) > 0:
        val = opPop()
        opPush(val)
        opPush(val)
        
    else:
        print("dup(): not enough values in opstack")

'''copy vals from opstack onto itself'''
def copy():
    
    valsToCopy = opPop()
    
    if len(opstack) >= valsToCopy:
        
        for i in range(valsToCopy):
            opPush(opstack[i])
            
    
    else:
        print("copy(): not enough values in opstack")

'''just calls opPop()'''
def pop():
    
    if len(opstack) > 0:
        return(opPop())
        
    else:
        print("pop(): not enough values in opstack")

'''clear opstack'''
def clear():
    
    if len(opstack) > 0:
        while len(opstack) != 0:
            opPop()

'''exchange top 2 values in opstack'''
def exch():
    
    if len(opstack) > 1:
        val1 = opPop()
        val2 = opPop()
        opPush(val1)
        opPush(val2)
    
    else:
        print("exch(): not enough values in opstack")

'''ex: "4 2 roll" --> move top 2 values on opstack into 4th stack position from top'''
def roll():
    
    if len(opstack) > 1:
        numValues = opPop()
        stackPos = opPop()        

        '''create a temporary stack that has all values that won't be touched in the rolling'''
        tempstack = []
        i = 0
        
        while i < stackPos:
            tempstack.append(opPop())
            i+=1
        
        if numValues > 0:
            '''seperate the rolled values from rest'''
            valsToPush = tempstack[:numValues]  #the numbers that are being rolled
            tempstack = tempstack[numValues:]       #the numbers going on top of the rolled numbers
            
            '''reverse the stacks so I can easily push them to opstack'''
            valsToPush = valsToPush[::-1]
            tempstack = tempstack[::-1]
            
            '''push rolled values in opstack'''
            for val in valsToPush:
                opPush(val)
                
            '''push values going on top of rolled values'''
            for val in tempstack:
                opPush(val)
        
        else:
            '''seperate the rolled values from rest'''
            valsToPush = tempstack[numValues:]
            tempstack = tempstack[:numValues]
            
            '''reverse stacks so I can easily push them to opstack'''
            valsToPush = valsToPush[::-1]
            tempstack = tempstack[::-1]
            
            '''push values going underneath of rolled values'''
            for val in tempstack:
                opPush(val)
                
            '''push rolled values in opstack'''
            for val in valsToPush:
                opPush(val)    
    else:
        print("roll(): not enough values in opstack")

'''display all contents of stack like the actual stack'''
'''edited for HW5'''
def stack():
    
    print("==============")

    for item in reversed(opstack):
        print(item)

    print("==============")
    
    for (index, item) in reversed(list(enumerate(dictstack))):
        level, dic = item
        print("----" +  str(index) + "----" + str(level) + "----")
        if dic:
            for val in dic:
                print(val, dic[val]) 

    print("==============")
        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DICTIONARY MANIPULATION OPERATORS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''creates/modifies dict entry in top dict on dictstack'''
def psDef():
    
    if len(opstack) > 1:
        value = opPop()
        name = opPop()
        define(name, value)
    
    else:
        print("psDef(): not enough values in dictstack")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    PART 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import re
def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HANDLING OF CODE-ARRAYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
''' psIf '''
def psIf(scope):
    
    if len(opstack) > 1:
        condition = opPop()
        operator = opPop()
        
        if operator == True:
            interpretSPS(condition, scope)
        
    else:
        print("psIf(): not enough values in opstack")

''' psIfelse '''
def psIfelse(scope):
    
    if len(opstack) > 2:
        condition_isFalse = opPop()
        condition_isTrue = opPop()
        operator = opPop()
        
        if operator == True:
            interpretSPS(condition_isTrue, scope)
            pass
        elif operator == False:
            interpretSPS(condition_isFalse, scope)
            pass
        else:
            print("psIfelse(): operator is not a bool")
            
    else:
        print("psIfelse(): not enough values in opstack")

''' psFor '''
def psFor(scope):
    
    if len(opstack) > 3:
        code = opPop()
        end = opPop()
        i = opPop()
        start = opPop()
        
        if isinstance(code, list):
            if i > 0:
                for x in range(start, end+1, i):
                    opPush(x)
                    interpretSPS(code, scope)
            
            if i < 0:
                for x in range(start, end-1, i):
                    opPush(x)
                    interpretSPS(code, scope)
        
        else:
            print("psFor(): cannot read code")
            
    else:
        print("psFor(): not enough values in opstack")
        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HELPER FUNCTIONS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
''' isIntOrFloat '''
def isIntOrFloat(c):
    
    try:
        complex(c)
        return True
    
    except(ValueError, TypeError):
        return False

''' isBoolean '''
def isBoolean(c):
    
    if c == "false" or c == "true":
        return True
    return False

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
''' groupMatching '''
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            res.append(groupMatching2(it))
        else:
            if isIntOrFloat(c) == True:
                ''' if float is same as int, it's int '''
                if int(c) == float(c):
                    c = int(c)
                else:
                    c = float(c)
            
            elif isBoolean(c) == True:
                '''if true, change to actual bool '''
                if c == "true":
                    c = True
                else:
                    c = False
            
            res.append(c)
            
    return False      

''' parse '''
def parse(L):
    res = []
    it = iter(L)
    
    for c in it:
        if c == '}':
            return False
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            if isIntOrFloat(c) == True:
                if c[0] == '(':
                    c = str(c)
                elif int(c) == float(c):
                    c = int(c)
                else:
                    c = float(c)
            elif isBoolean(c) == True:
                if c == "true":
                    c = True
                else:
                    c = False
            
            res.append(c)
    return res

''' spsOperators '''
def spsOperators(token, num, scope):
    
    spsOpDict = {'add':add, 'sub':sub, 'mul':mul, 'div':div, 'eq':eq, 'lt':lt, 'gt':gt, 
                 'if':psIf, 'ifelse':psIfelse, 'for':psFor, 'length':length, 'get':get,
                 'dup':dup, 'exch':exch, 'pop':pop, 'copy':copy, 'clear':clear, 'roll':roll,
                 'def':psDef, 'stack':stack, 'getinterval':getinterval, 'put':put}

    '''checking if true or false'''
    if num == 0:
        '''traverse thru every word in spsOpDict'''
        for word in spsOpDict:
            if word == token:               #if current word in spsOpDict == given token, call that function
                return True                
        else:
            return False
    
    #i already know its in spsOpDict, now just wanna call the function'''
    elif num == 1:
        for word in spsOpDict:
            if word == token:               #if current word in spsOpDict == given token, call that function
                if token == 'if' or token == 'ifelse' or token == 'for':
                    spsOpDict[token](scope)
                else:
                    spsOpDict[token]()

''' interpretSPS '''
def interpretSPS(code, scope): # code is a code array
    
    for token in code:
        if (isIntOrFloat(token) == True) or (isBoolean(token) == True) or (isinstance(token, list)) or token[0] == '(':
            opPush(token)
                
        elif isinstance(token, str):
            
            if token[0] == '/':
                opPush(token)
            
            elif spsOperators(token, 0, scope) == True: 
                spsOperators(token, 1, scope)
            
            else:
                
                (index, val) = lookup(token, scope)
                
                if val != None:

                    if isinstance(val, list):
                        dictPush((index, {}))
                        interpretSPS(val, scope)
                        dictPop()
                        
                    else:
                        opPush(val)
        
''' interpreter '''
def interpreter(s, scope): # s is a string
    interpretSPS(parse(tokenize(s)), scope)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TESTS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
input1 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic {
     /n 1 def
     /egg2 { n } def
     m n
     egg1
     egg2
     stack } def
    n
    chic
    """
    
input2 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    
input3 = """
    /out true def
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse
    dup /x exch def stack} def
    /myput { out dup /x exch def xand } def
    /f { /out false def myput } def
    false f
    """

allTests = {'input1':input1, 'input2':input2, 'input3':input3}

for testName in allTests:
    
    print("\n", str(testName) + ":")

    '''STATIC TESTING'''
    print("\nStatic")
    interpreter(allTests[testName], "static")
    clear()
    dictstack = []

    '''DYNAMIC TESTING'''
    print("\nDynamic")
    interpreter(allTests[testName], "dynamic")
    clear()
    dictstack = []   

