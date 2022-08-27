def PreprocessingGoodSuffix(pattern):

    arr=[]
    length=0         #length of suffix
    i=len(pattern)   #loop over pattern
    while(i>=0):
       i=i-1
       j=i-1       #to search in previous suffix
       length=length+1
       suffix=pattern[i:len(pattern)]
       #to loop over each and every possible match
       while(j>=0):
            cmpstring=pattern[j:(j+length)] #my goal is to match the closest first
            if(suffix==cmpstring): #first case
                 arr.append(i-j)
                 break
            elif(suffix != cmpstring and (j==1 or len(suffix) > len(pattern)/2)): #second case
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


def PreprocessingBadCharacter(sequence):
    myArr=[]
    length=len(sequence)
    for i in range(4):
        row=[]
        count=-1
        for j in range(length):
            if (sequence[j]== 'A' and i==0 ):
                row.append(-1)
                count=-1
            elif (sequence[j]=='C' and i==1 ):
                row.append(-1)
                count=-1
            elif (sequence[j]=='G' and i==2 ):
                row.append(-1)
                count=-1
            elif (sequence[j]=='T' and i==3 ):
                row.append(-1)
                count=-1
            else:
                count=count+1
                row.append(count)
        myArr.append(row)
    return myArr

def WholeBoyerMoore(text,pattern):
    arrGood=PreprocessingGoodSuffix(pattern)
    arrBad=PreprocessingBadCharacter(pattern)
    m=len(text)
    n=len(pattern)
    i=n-1
    j=i
    const=j
    while(j < m):
        while(i >=0 ):
            if(pattern[i]==text[const]):
                i=i-1
                const=const-1
            else:
                max1=arrGood[i]
                if(text[const]=='A'):
                    shift=arrBad[0][i]+1
                elif(text[const]=='C'):
                    shift=arrBad[1][i]+1
                elif(text[const]=='G'):
                    shift=arrBad[2][i]+1
                else:
                    shift=arrBad[3][i]+1
                if(shift<max1):
                   shift=max1
                j=j+shift
                const=j
                i=n-1
                break
            if(i==0):
                print("Found at index "+str(const))
                j=m
                break

WholeBoyerMoore("AAACAAAGCAGCAAACCGGTT","ACA")
WholeBoyerMoore("ATGGGGATCCCGACTCATCGAGG","ATCGAG")
WholeBoyerMoore("ACTGACTAACTCAAA","ACTCAAA")
WholeBoyerMoore("AACCGGTTTTTTACGTACGTTGCAGTCA","ACGT")
