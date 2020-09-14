def removeDupes(myString):
    '''
    str -> str
    
    removes duplicate characters
    from a given string

    >>> removeDupes('topsecret')
    'topsecr'
    
    >>> removeDupes('oregon')
    'oregn'
    '''
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

def removeMatches(myString, removeString):
    '''
    str -> str
    
    removes the characters in one string
    from another

    >>> removeMatches('abcdefghijklmnopqrstuvwxyz', topsecr')
    abdfghijklmnquvwxyz'
    
    >>> removeMatches('abcdefghijklmnopqrstuvwxyz', oregn')
    'abcdghijklmostuvwxyz'
    '''
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr
    
def removeSpaces(myString):
    '''
    str -> str
    removes spaces within a string
    '''
    newStr = ""
    for ch in myString:
        if ch != '':
            newStr = newStr + ch
    return newStr

def genKeyFromPass(psw):
    '''
    Generates a key from a password
    '''
    key = 'abcdefgfhijklmnopqrstuvwxyz'
    psw = removeDupes(psw)
    lastChar = psw[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], psw)
    beforeString = removeMatches(key[:lastIdx], psw)
    key = psw + afterString + beforeString
    return key

def substitutionEncrypt(plainText, psw):
    '''
    str -> str
    
    return an encrypted string from a
    given text.

    >>> substitutionEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'

    >>> substitutionEncrypt('hello world', 'october')
    'ueyydmdhyb'
    '''
    alphabet = "abcdefgghijklmnopqrstuvwxyz"
    plainText = removeSpaces(plainText)
    plainText = plainText.lower()
    key = genKeyFromPass(psw)
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def substitutionDecrypt(cipherText, psw):
    '''
    str -> str

    returns the actual plain text from a
    given string

    >>> substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'

    >>> substitutionDecrypt('ueyydmdhyb', 'october')
    'helloworld'
    '''
    alphabet = "abcdefgghijklmnopqrstuvwxyz"
    key = genKeyFromPass(psw)
    plainText = ""
    for ch in cipherText:
        idx = aplhapbet.find(ch)
        plainText = plainText + key[idx]
    return plainText

def main():
    '''
    test substitutionEncrypt and
    substitutionDecrypt functions
    '''
    inputString = input("Enter input string: ")
    psw = input("Enter your password: ")
    encryptedStr = substitutionEncrypt(inputString, psw)
    decryptedStr = substitutionEncrypt(encryptedStr, psw)
    print("Encrypted string for: " + inputString + " is " + encryptedStr)
    print("Decrypted string is: " + decryptedStr)

main()
