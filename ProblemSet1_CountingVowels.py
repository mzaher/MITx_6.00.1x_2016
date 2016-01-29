def countVowels(s):
    """set the vowels to its know value string, and set a counter variabl to iniate value of 0 
    check if the vowel cahracter is in the given string s, looping every character in s string 
    and check if it is one of the vowels string. If so, the counter increment by 1 
    and print out the number of counted vowels.
"""

    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            countPrint = 'Number of vowels: %s' % count 
    return countPrint

def printCount():
    print(countVowels(s))

printCount()