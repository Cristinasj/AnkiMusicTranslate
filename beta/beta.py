import sys

def linesMatch (x, y):
    return x.count('\n') == y.count('\n')

print ("Write the whole lyrics in your native tongue (cntl+D to stop): ")
native = sys.stdin.read()
print('Write the lyrics in your target language formated with clozes, you might want to do that step in anki (cntl+D to stop): ')
target = sys.stdin.read()

if (linesMatch(native,target)):
    linesCount = native.count('\n')
    native = native.splitlines()
    target = target.splitlines(keepends=True)
    result = ''
    for lineNum in range(linesCount):
        result += native[lineNum] + '  ' + target[lineNum]
    print('This is the formated result: ')
    print(result)
else:
    print('The number of lines does not match')
