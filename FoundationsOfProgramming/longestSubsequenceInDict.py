import numpy as np # Bring numpy in for indexing via mask

d = ["able", "ale", "hullabuloo", "apple"] # Here is our dictionary
subsq = [] # emtpy array to hold all of our subsequences

def yieldSubSq(s_, d):
    '''
    arguments:
    s_ string: Master sequence containig subsequences
    d list of strings: dictionary of words to check
    '''
    for w in d: # For each word in the dictionary
        s = s_ # let s be our master string
        print(f"Word: {w}")
        isSubSq=True # Assume all words are subsequences until proven otherwise
        for l in w: # for each leter in the word w
            isInSq=False # keep track of whether the letter l is in our master sequence
            for i in range(len(s)-1): # for each letter i the master sequence
                if(l==s[i]): # if the letter l is in the sequence
                    s=s[i+1:] # remove every letter in master sequence up to the current letter
                    isInSq=True # letter l is in the sequence
                    break 
            if(isInSq==False): # if letter l wasn't in the sequence 
                isSubSq=False # the word is not a subsequence
                break
        if(isSubSq): # if the word is a subsequence
            yield w # yield it


                
s = "abppplee" # define the master sequence
subSqGen = yieldSubSq(s, d)  # declare the generator of subsequences

for subSq in subSqGen: 
    subsq.append(subSq) # yield all available subsequences in dictionary

subsq=np.array(subsq) # convert to numpy array for boolean indexing
lengths = np.array(list(map(len, subsq))) # Create array of lengths of each subsequence
print(subsq[np.where(lengths==np.max(lengths))]) # print out the longest subsequence