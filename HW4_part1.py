'''
NAME:       DANIEL HARKER
ID:         11513968
DATE:       22 Mar 2019
ASSIGNMENT: HW4 Part 1
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
        func = opPop()
        
        if func == "dup" or func == "def":
            
            if func == "dup":
                dup()
                string = opPop()
            
            elif func == "def":
                string = opPop()
                name = opPop()
                define(name, string)
                
            strToList = list(string)    #turn the string in to a list so I can manipulate it
            strToList[index] = chr(asciiVal)
            string = "".join(strToList)
            opPush(string)
             
        else:
            print("put(): something is wrong")  
            
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
TEST FUNCTIONS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def testDefine():
    dictPush({})
    define("/n1", 4)
    if lookup("n1") != 4:
        print("FAIL - deduct:",-2)
        return False
    print("PASS")
    return True

def testLookup():
    dictPush({'/v':3})
    dictPush({'/v':4})
    dictPush({'/v':5})
    if lookup("v") != 5:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

def testAdd():
    opPush(9)
    opPush(-2)
    add()
    if opPop() != 7:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testSub():
    opPush(10)
    opPush(2)
    sub()
    x = opPop()
    if x == -8:
        print("FAIL - The order of the arguments for 'sub' are reversed - deduct:", -1)
        return False
    elif x != 8:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testMul():
    opPush(2)
    opPush(40)
    mul()
    if opPop() != 80:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testDiv():
    opPush(12)
    opPush(3)
    div()
    x = opPop()
    if x == 0.25:
        print("FAIL - The order of the arguments for 'div' are reversed - deduct:", -1)
        return False
    elif x != 4:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testMod():
    opPush(10)
    opPush(4)
    mod()
    x = opPop()
    if x == 0:
        print("FAIL - The order of the arguments for 'mod' are reversed - deduct:", -1)
        return False
    elif x != 2:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testLt():
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

def testGt():
    opPush(4)
    opPush(5)
    gt()
    if opPop() != False:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

def testEq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testLength():
    opPush("(CptS355 HW4)")
    length()
    l = opPop()
    if l == 13:
        print("FAIL - (should not count paranthesis as part of the string) deduct:", -2)
        return False
    elif l != 11:
        print("FAIL - deduct:", -4)
        return False
    print("PASS")
    return True

def testGet():
    opPush("(CptS355 HW4)")
    opPush(10)
    get()
    c = opPop()
    if c == 87:
        print("FAIL - (delimiter paranthesis are not part of the string; the 10th character is 4 ; not W) deduct:", -3)
        return False
    elif c== 'W' or c =='4':
        print("FAIL - (get should push the ASCII value of the character onto the stack) deduct:", -3)
        return False
    elif c != 52:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

def testGetinterval():
    opPush("(CptS355 HW4)")
    opPush(8)
    opPush(3)
    getinterval()
    c = opPop()
    if c == '( HW)':
        print("FAIL - (delimiter paranthesis are not part of the string; getinterval returns (HW4) ; not ( HW);  deduct:", -3)
        return False
    elif c == 'HW4':
        print("FAIL - (the returned substring should be enclosed in paranthesis;  deduct:", -3)
        return False
    elif c != '(HW4)':
        print("FAIL - (In this test case 8 is the starting index for the substring and 3 is the length of the substring. deduct:", -5)
        return False
    print("PASS")
    return True

def testPut():
    opPush("CptS355")
    opPush("dup")
    opPush(6)
    opPush(48)
    put()
    if opPop() != "CptS350":
        return False
    return True


def testDup():
    opPush("(CptS355 HW4)")
    dup()
    if opPop()!=opPop():
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

def testExch():
    opPush("/x")
    opPush(5)
    exch()
    if opPop()!="/x" and opPop()!=5:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if l1!=l2:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

def testRoll():
    '''test rolling from top to in stack'''
    clear()
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(6)
    opPush(7)
    opPush(8)
    opPush(4)
    opPush(2)
    roll()
    if opstack != [1, 2, 3, 4, 7, 8, 5, 6]:
        return False
    '''test rolling from in stack to top'''
    clear()
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(True)
    opPush(1)
    opPush('(12)')
    opPush(3)
    opPush(4)
    opPush(3)
    copy()
    if opPop()!=4 and opPop()!=3 and opPop()!='(12)' and opPop()!=4 and opPop()!=3 and opPop()!='(12)' and opPop()!=1:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        print("FAIL - deduct:", -3)
        return False
    elif len(opstack)>0:
        print("FAIL - psDict should pop the size argumen from the stack ; deduct:", -2)
        return False
    print("PASS")
    return True

def testBeginEnd():
    dictPush({})
    opPush("/x")
    opPush(3)
    psDef()
    opPush(1)
    psDict()
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end() #SUT
    if lookup("x")!=3:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

def testpsDef():
    dictPush({})
    opPush("/x")
    opPush(10)
    psDef()
    opPush("/x")
    opPush(20)
    psDef()
    if lookup("x")==10:
        print("FAIL - deduct:", -4, "(psDef should overwrite the existing definition : -5 +1 partial points)")
        return False
    elif lookup("x")!=20:
        print("FAIL - deduct:", -5)
        return False

    print("PASS")
    return True

def testpsDef2():
    dictPush({})
    opPush("/x")
    opPush(10)
    psDef()
    opPush(2)
    psDict()
    begin()
    opPush("/y")
    opPush(20)
    psDef()
    if lookup("x")!=10:
        end()
        print("FAIL - deduct:", -5)
        return False
    end()
    print("PASS")
    return True

def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),
                 ('div', testDiv),  ('mod', testMod), ('lt', testLt), ('gt', testGt), ('eq', testEq),
                 ('length', testLength),('get', testGet), ('getinterval', testGetinterval),
                 ('put', testPut), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll),
                 ('copy', testCopy), ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd),
                 ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    print(main_part1())




