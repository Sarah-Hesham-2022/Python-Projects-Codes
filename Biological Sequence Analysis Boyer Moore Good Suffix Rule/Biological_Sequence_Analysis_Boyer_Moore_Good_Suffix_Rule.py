def PreprocessingGoodSuffix(pattern):

    arr=[]
    length=0         #length of suffix
    i=len(pattern)   #loop over pattern
    while(i>=0):
       i=i-1
       j=i-1       #to search in previous suffix
       match=""
       length=length+1
       suffix=pattern[i:len(pattern)]
       #to loop over each and every possible match
       while(j>=0):
            cmpstring=pattern[j:(j+length)] #my goal is to match the closest first
            if(suffix==cmpstring): #first case
                 arr.append(i-j)
                 break
            elif(suffix != cmpstring and (j<=1 or len(suffix) > len(pattern)/2)): #second case
                 maxLength=len(suffix) #length of suffix
                 m=0
                 prefixLength=len(pattern)-maxLength
                 while(prefixLength>=0):
                     prefix=pattern[0:(prefixLength)] #my goal is to match the longest possible first
                     if(maxLength>prefixLength):
                         m=(maxLength-prefixLength)
                     prefixLength=prefixLength-1
                     cmpToPrefix=suffix[m:]
                     if(prefix==cmpToPrefix):
                         arr.append(len(pattern)-len(prefix))
                         break
                     else:
                         m=m+1
                 break
            j=j-1

    arr.append(len(pattern)) #case three as first element is going to be totally shifted by length of the pattern
    arr.reverse()            #reverse array as I was looping from right to left
    return arr

print(PreprocessingGoodSuffix("AABCGTBA"))
print(PreprocessingGoodSuffix("BAOBAB"))
print(PreprocessingGoodSuffix("GGG"))
print(PreprocessingGoodSuffix("CTTACTTAC"))
print(PreprocessingGoodSuffix("GTAGCGGCG"))
print(PreprocessingGoodSuffix("AAAACCGGTTACGT"))
print(PreprocessingGoodSuffix("ABA"))
print(PreprocessingGoodSuffix("TATGTG"))
print(PreprocessingGoodSuffix("ACTCAAA"))

def BoyerMooreGoodSuffix(text,pattern):
    arr=PreprocessingGoodSuffix(pattern)
    shift = 0
    m=len(text)
    n=len(pattern)
    i = n-1
    j = i
    const=j
    while(j < m):
         while(i >= 0 ):
              if (pattern[i] == text[const]):
                 const=const-1
                 i=i-1
                 shift=0
              else:
                 shift =arr[i]
                 j=shift+j
                 const=j
                 i = n-1
                 break
              if (i ==0 and shift==0):
                 print("pattern occurs at shift = " + str(const))
                 j=m
                 break


BoyerMooreGoodSuffix("BESS_KNEW_ABOUT_BAOBABS","BAOBAB")
BoyerMooreGoodSuffix("CGTTTCCAAGGGCCTACTTACTTACTTACTTACGCGAATCTAAGGTT","CTTACTTAC")
BoyerMooreGoodSuffix("GTTATAGCTGATCGCGGGCGTAGCGGCGAATCGAAT","GGG")
BoyerMooreGoodSuffix("ABAAAABAACD","ABA")
BoyerMooreGoodSuffix("ACTGACTAACTCAAA","ACTCAAA")
