'''
NAME:       DANIEL HARKER
ID:         11513968
DATE:       3 Apr 2019
ASSIGNMENT: HW4 Part 2
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
    # dictPop pops the top dictionary from the dictionary stack.

'''push value to end of dictstack'''
def dictPush(d):
    
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

'''add name:value to top dict in dictstack'''
def define(name, value):
    
    '''if not empty, add name:value pair to top dict'''
    '''else, create a new dict and push it to dictstack via dictPush'''
    if len(dictstack) > 0:
        dictstack[(len(dictstack)) - 1][name] = value
        
    else:
        newDict = {}
        newDict[name] = value
        dictPush(newDict)
    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant. 
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

'''looks up name in dicionaries of dictstack. if found, return the value'''
def lookup(name):
    
    for item in range(len(dictstack)):
        dic = dictstack[len(dictstack) - 1 - item]
        if ('/' + name) in dic.keys():
            return dic['/' + name]
        
    return None
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

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
        
#        ''' change the original and opPush '''
#        if string[0] == '(':
#            string = string[1: (len(string) - 1)]
#            
#        strToList = list(string)
#        strToList[index] = chr(asciiVal)
#        string = "".join(strToList)
#        opPush('(' + string + ')')
            
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
    
    else:
        print("clear(): osptack is already cleared")

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
def stack():
    
    print(opstack)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DICTIONARY MANIPULATION OPERATORS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''takes initial size of dict from stack, puts brand new empty dict on operand stack'''
def psDict():
    
    if len(dictstack) > 0:
        opPop()
        opPush({})
    
    else:
        print("psDict(): not enough values on dictstack")

'''takes dict from opstack and pushes to dictstack'''
def begin():
    
    if len(opstack) > 0:
        dictPush(opPop())
        
    else:
        print("begin(): not enough values on opstack")

'''pop top dict from dictstack and throw it away'''
def end():
    
    if len(dictstack) > 0:
        dictPop()
    
    else:
        print("end(): not enough values in dictstack")

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
def psIf():
    
    if len(opstack) > 1:
        condition = opPop()
        operator = opPop()
        
        if operator == True:
            interpretSPS(condition)
        
    else:
        print("psIf(): not enough values in opstack")

''' psIfelse '''
def psIfelse():
    
    if len(opstack) > 2:
        condition_isFalse = opPop()
        condition_isTrue = opPop()
        operator = opPop()
        
        if operator == True:
            interpretSPS(condition_isTrue)
            pass
        elif operator == False:
            interpretSPS(condition_isFalse)
            pass
        else:
            print("psIfelse(): operator is not a bool")
            
    else:
        print("psIfelse(): not enough values in opstack")

''' psFor '''
def psFor():
    
    if len(opstack) > 3:
        code = opPop()
        end = opPop()
        i = opPop()
        start = opPop()
        
        if isinstance(code, list):
            if i > 0:
                for x in range(start, end+1, i):
                    opPush(x)
                    interpretSPS(code)
            
            if i < 0:
                for x in range(start, end-1, i):
                    opPush(x)
                    interpretSPS(code)
        
        else:
            print("psFor(): cannot read code")
            
    else:
        print("psFor(): not enough values in opstack")
        
''' psAnd '''
''' not necessary for HW4.2, but helps input4 work '''
def psAnd():
    
    if len(opstack) > 1:
        bool1 = opPop()
        bool2 = opPop()
        
        if (bool1 == True) and (bool2 == True):
            opPush(True)
        
        else:
            opPush(False)
            
    else:
        print("psAnd(): not enough values in opstack")

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
  
# complete this function
# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
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
def spsOperators(token, num):
    
    spsOpDict = {'add':add, 'sub':sub, 'mul':mul, 'div':div, 'eq':eq, 'lt':lt, 'gt':gt, 
                 'if':psIf, 'ifelse':psIfelse, 'for':psFor, 'length':length, 'get':get,
                 'dup':dup, 'exch':exch, 'pop':pop, 'copy':copy, 'clear':clear, 'roll':roll,
                 'begin':begin, 'end':end, 'def':psDef, 'dict':psDict, 'stack':stack, 'getinterval':getinterval, 'put':put, 'and':psAnd}

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
                spsOpDict[word]()

''' interpretSPS '''
def interpretSPS(code): # code is a code array
    
    for token in code:
#        print('\n curToken: ', token, type(token))
#        stack()
#        print(dictstack)
        if (isIntOrFloat(token) == True) or (isBoolean(token)) or (isinstance(token, list)) or token[0] == '(':
            opPush(token)
                
        elif isinstance(token, str):
#            print("isStr")
            
            if token[0] == '/':
                opPush(token)
            
            elif spsOperators(token, 0) == True:
                spsOperators(token, 1)
            
            else:
#                print("FAIL")
                val = lookup(token)
#                print("VAL: ", val)
                if not isinstance(val, list): 
#                    print("OTHER")
                    opPush(val)
                else:
                    interpretSPS(val)

            
#        print("opstack:   ", opstack)
#        print("dictstack: ", dictstack)
        
''' interpreter '''
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TESTS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

input1 = """
        /square {
               dup mul
        } def 
        (square)
        4 square 
        dup 16 eq 
        {(pass)} {(fail)} ifelse
        stack 
        """

input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
        end
    } def
    n fact stack
    """

input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """

input4 = """
        /lt6 { 6 lt } def 
        1 2 3 4 5 6 4 -3 roll    
        dup dup lt6 {mul mul mul} if
        stack 
    """

input5 = """
        (CptS355_HW5) 4 3 getinterval 
        (355) eq 
        {(You_are_in_CptS355)} if
         stack 
        """

input6 = """
        /pow2 {/n exch def 
               (pow2_of_n_is) dup 8 n 48 add put 
                1 n -1 1 {pop 2 mul} for  
              } def
        (Calculating_pow2_of_9) dup 20 get 48 sub pow2
        stack
        """

allResults = []

'''input 1'''
print("input1:")
interpreter(input1)
if opstack != ['(square)', 16, '(pass)']:
    allResults.append("input1")  
clear()
dictstack = []

'''input 2 '''
print("\ninput2:")
interpreter(input2)
if opstack != ['(facto)', 120]:
    allResults.append("input2")
clear()
dictstack = []

''' input 3 '''
print("\ninput3:")
interpreter(input3)
if opstack != [720]:
    allResults.append("input3")
clear()
dictstack = []

''' input 4 '''
print("\ninput4:")
interpreter(input4)
if opstack != [1, 2, 6, 300]:
    allResults.append("input4")
clear()
dictstack = []

''' input 5 '''
print("\ninput5:")
interpreter(input5)
if opstack != ['(You_are_in_CptS355)']:
    allResults.append("input5")
clear()
dictstack = []

''' input 6 '''
print("\ninput6:")
interpreter(input6)
if opstack != ['(Calculating_pow2_of_9)', '(pow2_of_9_is)', 512]:
    allResults.append("input6")
clear()
dictstack = []


''' CHECK RESULTS '''
if allResults == []:
    print("\nAll tests passed!")
    
else:
    print("\nFailed tests: ")
    for test in allResults:
        print(test)
        
#opstack = [1,2,3,4,5,6,4,-3]
#roll()
#dup()
#dup()
#opPush([6, 'lt'])
#exch()
#opPush(3)
#gt()
#psAnd()
##opPush([mul, mul])
##psIf()
#stack()



