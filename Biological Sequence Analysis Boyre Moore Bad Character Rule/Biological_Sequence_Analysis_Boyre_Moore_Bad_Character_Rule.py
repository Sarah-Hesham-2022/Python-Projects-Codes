#This function is to get the table that will direct our moves

def createTable(sequence):
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

#This just a nice formatting to print the table in a nice way

def printTable(sequence):
        table=createTable(sequence)
        print("My Table of Indices Move Boyer Moore :\n")
        print("  ",end='')
        for i in sequence:
            print("  "+i,end='')
        for i in range(4):
            if (i==0):
                    print("\nA   ",end='')
            elif (i==1):
                    print("\nC   ",end='')
            elif (i==2):
                    print("\nG   ",end='')
            else:
                    print("\nT   ",end='')
            for j in table[i]:
                if(j==-1):
                    j='-'
                print(str(j) +"  ",end='')
        print("\n\n")

#Boyer Moore
def BadCharacterRule(text,seq):
    if(len(seq)>len(text)):
        print("Not Found\n")
        print(text)
        print(seq)
        print("\n")
        return False
    table=createTable(seq)
    i=len(seq)-1
    while( i < len(text)):
        temp=i #Becareful, this step is so important as we need to keep something to say where we would increment by sequence length and another thing to iterate
        j=len(seq)-1
        move=0
        while( j >= 0):
           if(text[i]=='A'):
               move=table[0][j]+1
           elif(text[i]=='C'):
               move=table[1][j]+1
           elif(text[i]=='G'):
               move=table[2][j]+1
           else:
               move=table[3][j]+1
           if(move!=0):
               i=temp+move
               break
           if(move==0 and j==0):
               print("Found at index "+str(i))
               for m in text:
                   print(m+"-",end='')
               print("\n",end='')
               print("  " * i,end='')
               for m in seq :
                   print(m+"-",end='')
               print("\n")
               return True
           j=j-1
           i=i-1
    print("Not Found\n")
    print(text)
    print(seq)
    print("\n")
    return False


#My Main
printTable("TCGC")
print(BadCharacterRule("AATCAATCGC","TCGC"))

print("--------------------------------------------------------")
printTable("TCGCCCGGAATTGCG")
print(BadCharacterRule("AATCAATCGC","TCGCCCGGAATTGCG"))

print("--------------------------------------------------------")
printTable("CCGGAATTGCG")
print(BadCharacterRule("GCTAAATCCGGAATTGCGCCCTTAA","CCGGAATTGCG"))

print("--------------------------------------------------------")
printTable("GGATTGG")
print(BadCharacterRule("GCTAAATCCGGATTGGCCCTTAA","GGATTGG"))


print("--------------------------------------------------------")
printTable("GGATTGG")
print(BadCharacterRule("GCTAAATCCTTGGCCCTTAA","GGATTGG"))