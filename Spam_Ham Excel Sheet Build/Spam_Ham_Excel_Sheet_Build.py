# Writing to an excel 
# sheet using Python
#If you don't have it ,open console in python and type : 

#pip install XlsxWriter

import xlsxwriter
from xlsxwriter import Workbook
  
# Workbook is created
workbook = xlsxwriter.Workbook('Sheet Numerical Data.xlsx')
  
# add_sheet is used to create sheet.
sheet1 = workbook.add_worksheet()

#sheet1.write(row, col, data)
  

myFile=open("C:/Users/Sarah Hesham/OneDrive/Documents/Python/Spam_Ham Excel Sheet Build/Spam_Ham/File.txt")

line=myFile.readline()
msgType=line[0:4]
count=1

arrMsgs=[]
arrWords=[]
arrUniqueWords=[]

sheet1.write(0,0,"Label")

while(line):
    if(msgType=="spam"):
        #sheet1.write(count, 1, line[4:])
        sheet1.write(count, 0, 1)
        arrMsgs.append(line[4:].lstrip().rstrip())

    else:
        #sheet1.write(count, 1, line[3:])
        sheet1.write(count, 0,0)
        arrMsgs.append(line[3:].lstrip().rstrip())

    line=myFile.readline()
    msgType=line[0:4]
    count=count+1

for i in arrMsgs:
    arrWords.append(i.split(" "))

for i in arrWords:
    for j in i:
        if not(j in arrUniqueWords):
            arrUniqueWords.append(j)

count=1

while(count <= len(arrUniqueWords)):
    sheet1.write(0, count, arrUniqueWords[count-1])
    count=count+1

for i in range(len(arrUniqueWords)):
    for j in range(len(arrMsgs)):
        number=0
        temp=arrMsgs[j].split(" ")
        for z in temp:
            if(z==arrUniqueWords[i]):
                number=number+1
        sheet1.write(j+1,i+1,number)

#Essential to save the work
workbook.close()