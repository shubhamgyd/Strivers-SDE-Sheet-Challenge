def generateSubsequences(index, currentSubsequence, str, n):
    if index == n:
        if len(currentSubsequence) != 0:
            return [currentSubsequence]
        return []
    # Take
    subsequences = generateSubsequences(index+1, currentSubsequence + str[index], str, n)
    
    # Do not Take
    subsequences += generateSubsequences(index+1, currentSubsequence, str, n)
    
    return subsequences

def subsequencs(input_str):
    n = len(input_str)
    print(generateSubsequences(0,'',input_str,len(input_str)))

subsequencs(['a','b','c'])
