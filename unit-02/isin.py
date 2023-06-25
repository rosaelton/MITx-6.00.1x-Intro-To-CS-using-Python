def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False

    midchar = aStr[len(aStr) // 2]

    if midchar == char:
        return True

    if midchar < char:
        return isIn(char, aStr[len(aStr) // 2 + 1:])

    return isIn(char, aStr[:len(aStr) // 2])
