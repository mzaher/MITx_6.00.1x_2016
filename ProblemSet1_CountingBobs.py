search = 'bob'

def countVowels(s):
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == search:
            count += 1
    countPrint = ("Number of times %s occurs is: %s" %  (search, count))
    return countPrint

def printCount():
    print(countVowels(s))
printCount()
