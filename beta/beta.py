import sys

def linesMatch (x, y):
    return x.count('\n') == y.count('\n')

def isComment(s):
    return s[0] == '['

def isLongEnough(x):
    return len(x) > 3

def clozeDebug(x):
    result = []
    added = []
    clozeCount = 1
    index = 1
    chars = " \n,.-;:_\t"
    for line in x:
        if isLongEnough(line):
            if line.strip(chars) in added:
                index = added.index(line.strip(chars)) + 1
                print(str(index))
            else:
                index = clozeCount
                clozeCount += 1
                added.append(line.strip(chars))
            result.append('{{c' + str(index) + '::' + line + '}}' + '\n')
        else:
            result.append('\n')
    return result

# Prior cloze function
# It added every line equal or not
def clozeRepeating(x):
    result = []
    added = []
    clozeCount = 1
    index = 1
    chars = " \n,.-;:_\t"
    for line in x:
        if isLongEnough(line):
            if line.strip(chars) in added:
                index = added.index(line.strip(chars)) + 1
            else:
                index = clozeCount
                clozeCount += 1
                added.append(line.strip(chars))
            result.append('{{c' + str(index) + '::' + line + '}}' + '\n')
        else:
            result.append('\n')
    return result

def cloze(x): 
    result = []
    added = []
    index = 1
    chars = "\n,.-;:_\t"
    for line in x:
        # Does not maintain punctuation
        line = line.strip(chars) 
        # Does not add repeated lines 
        if isLongEnough(line) and not line in added:
            result.append('{{c' + str(index) + "::" + line + "}}" + "\n")
            added.append(line)
            index += 1
        else: 
            result.append("\n") 

    return result



def format(native, target):
    linesCount = native.count('\n')
    native = native.splitlines()
    target = target.splitlines()
    target = cloze(target)
    result = ''
    for lineNum in range(linesCount):
        result += native[lineNum] + '  ' + target[lineNum]
    return result

print('\nWrite the lyrics in your target language (cntl+D to stop): \n')
target = sys.stdin.read()

print ("\nWrite the whole lyrics in your native tongue (cntl+D to stop): \n")
native = sys.stdin.read()

if (linesMatch(native,target)):
    result = format(native,target)
    print('\nThis is the formated result: \n')
    print(result)
else:
    print('\n [ERROR] The number of lines does not match\n')
    if native.count('\n') > target.count('\n'):
        print ('\n [ERROR] The lyrics in your native tongue are longer\n')
    else:
        print ('\n [ERROR] The lyrics in your target language are longer\n')
