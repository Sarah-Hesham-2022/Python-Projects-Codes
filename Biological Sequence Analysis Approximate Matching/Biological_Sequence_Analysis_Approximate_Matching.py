def createArrayEditDistance(PatternA,PatternB):

    array=[]

    #initialzie array with many rows of zeroes
    for i in range (len(PatternA)+1):
        array.append([0]*(len(PatternB)+1))

    #initialize first column with 0,1,2,3,....
    for i in range (len(PatternA)+1):
        array[i][0]=i

    #initialize first row with 0,1,2,3,....
    for i in range(len(PatternB)+1):
        array[0][i]=i

    #Fill the array
    for i in range (1,len(PatternA)+1):
        for j in range (1,len(PatternB)+1):
            distHorizontal = array[i][j-1]+1
            distVertical   = array[i-1][j]+1
            if(PatternA[i-1]==PatternB[j-1]):
                distDiagonal=array[i-1][j-1]
            else:
                distDiagonal=array[i-1][j-1]+1

            #take min of the 3 
            array[i][j]=min(distHorizontal,distVertical,distDiagonal)
    return array


print(createArrayEditDistance("GCGTATGCACGC","GCTATGCCACGC"))
print("\n\n")
print(createArrayEditDistance("GCGTATGCGGCTAACGC","GCTATGCGGCTATACGC"))
print("\n\n")
print(createArrayEditDistance("the longest day","the longest"))
print("\n\n")
print(createArrayEditDistance("AACCCTATGTCATGCCTTGGA","TACGTCAGC"))
print("\n\n")

#This function prints the corresponding matches and edits and deletes
def getSequence(PatternA,PatternB):

    #create the 2D array
    array=createArrayEditDistance(PatternA,PatternB)

    #Get last row
    lastRow=array[-1]

    lastRowMin=10000000
    index=-1
    sequence=""

    #Get min element and its index in the last row from which the dynammic programming should start
    for i in range (len(lastRow)):
        if(lastRowMin > lastRow[i]):
            lastRowMin=lastRow[i]
            index=i
    
    #Now let us go back one row
    i=len(PatternA)-1

    #loop over the array
    while(i>=0):
        elemHorizontal=array[i+1][index-1]
        elemVertical=array[i][index]
        elemDiagonal=array[i][index-1]
        minElem=min(elemHorizontal,elemVertical,elemDiagonal)

        #If the min element is the diagonal, we are a match and just move the index back one step
        if(minElem==elemDiagonal):
            sequence=sequence+PatternB[index-1]
            index=index-1

        #If the min element is the vertical one, this is a delete and here we don't decrease the index as we move vertically
        elif(minElem==elemVertical):
             sequence=sequence+"-"
         
     #If the min element is the horizontal one,this is a insert and we decraese the index by 2 as we move 2 steps back
        else:
            sequence=sequence+"-"
            index=index-2
        #Go to previous row
        i=i-1
    print(PatternA)
    #return the string but in reverse as we in backtracking were moving from end of string to begginig
    return  "".join(reversed(sequence))

print("\n\n")
print(getSequence("GCGTATGCACGC","GCTATGCCACGC"))
print("\n\n")
print(getSequence("GCGTATGCGGCTAACGC","GCTATGCGGCTATACGC"))
print("\n\n")
print(getSequence("the longest day","the longest"))
print("\n\n")
print(getSequence("AACCCTATGTCATGCCTTGGA","TACGTCAGC"))
print("\n\n")