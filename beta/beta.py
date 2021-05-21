import sys

def linesMatch (x, y):
    return x.count('\n') == y.count('\n')

def clozeDebug(x):
    result = []
    added = []
    clozeCount = 1
    index = 1
    chars = " \n,.-;:_\t"
    for line in x:
        if len(line) > 5:
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
    for line in added:
        print(line)
    return result

def cloze(x):
    result = []
    added = []
    clozeCount = 1
    index = 1
    chars = " \n,.-;:_\t"
    for line in x:
        if len(line) > 5:
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



def format(native, target):
    linesCount = native.count('\n')
    native = native.splitlines()
    target = target.splitlines()
    target = cloze(target)
    result = ''
    for lineNum in range(linesCount):
        result += native[lineNum] + '  ' + target[lineNum]
    return result

print ("\nWrite the whole lyrics in your native tongue (cntl+D to stop): \n")
native = sys.stdin.read()
print('\nWrite the lyrics in your target language formated with clozes, you might want to do that step in anki (cntl+D to stop): \n')
target = sys.stdin.read()

if (linesMatch(native,target)):
    result = format(native,target)
    print('\nThis is the formated result: \n')
    print(result)
else:
    print('\nThe number of lines does not match\n')
    if native.count('\n') > target.count('\n'):
        print ('\nThe lyrics in your native tongue are longer\n')
    else:
        print ('\nThe lyrics in your target language are longer\n')
