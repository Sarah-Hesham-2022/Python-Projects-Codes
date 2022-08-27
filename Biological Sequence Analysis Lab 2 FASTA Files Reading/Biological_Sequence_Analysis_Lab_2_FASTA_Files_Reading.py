#Task:

#-	Write a function that reads a FASTA file to extract the genome from it

myFile=open("phix.fa")
def Extract(myFile):
    genome=""
    line =myFile.readline()
    while(line):
        if(line[0]==">"):
            line=myFile.readline()
        else:
            genome=genome+line
            line=myFile.readline()
    return genome

genome=Extract(myFile)
print(genome)

#-	Write a match function that takes the pattern P and the text T. This function should return the indices of the exact matching P inside the text T.
def matchingIndices(pattern,text):
    myArr=[]
    match=""
    l=len(pattern)
    i=0
    while(i<len(text)):
        while(len(match)<l and i<len(text)):
            match=match+text[i]
            i=i+1
        if(match==pattern):
            myArr.append(i-l)
        match=match[len(match)-1]
    return myArr

print(matchingIndices("AG","AGCTTAGATAGCAGAGAGTTAG"))



