import sys

def linesMatch (x, y):
    return x.count('\n') == y.count('\n')

def cloze(target):
    result = []
    added = []
    i = 1
    for line in target:
        if line in added:
            if len(line) > 5:
                index = added.index(line)
                result.append('{{c' + str(index-1) + '::' + line + '}}' + '\n')
            else:
                result.append('\n')
        else:
            if len(line) > 5: 
                result.append('{{c' + str(i) + '::' + line + '}}' + '\n')
                i += 1
            else:
                result.append('\n')
        added.append(line)
            
    return result
    

def format(native, target):
    linesCount = native.count('\n')
    print(linesCount)
    native = native.splitlines()
    target = target.splitlines()
    target = cloze(target)
    result = ''
    for lineNum in range(linesCount):
        result += native[lineNum] + '  ' + target[lineNum]
    return result

print ("Write the whole lyrics in your native tongue (cntl+D to stop): ")
native = sys.stdin.read()
print('Write the lyrics in your target language formated with clozes, you might want to do that step in anki (cntl+D to stop): ')
target = sys.stdin.read()

if (linesMatch(native,target)):
    result = format(native,target)
    print('This is the formated result: ')
    print(result)
else:
    print('The number of lines does not match')
