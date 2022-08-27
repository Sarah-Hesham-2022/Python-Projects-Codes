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
  
myFile=open("C:/Users/Sarah Hesham/OneDrive/Documents/Python/Heart Disease File Processing/Heart Data.data")

line=myFile.readline()

sheet1.write(0,0,"Age")
sheet1.write(0,1,"Sex")
sheet1.write(0,2,"CP")
sheet1.write(0,3,"Trestbps")
sheet1.write(0,4,"Chol")
sheet1.write(0,5,"fbs")
sheet1.write(0,6,"Restecg")
sheet1.write(0,7,"Thalach")
sheet1.write(0,8,"Exang")
sheet1.write(0,9,"Oldpeak")
sheet1.write(0,10,"Slope")
sheet1.write(0,11,"Ca")
sheet1.write(0,12,"Thal")
sheet1.write(0,13,"Prediction")

arrRows=[]

while(line):
    newLine=line.split(",")
    arrRows.append(newLine)
    line=myFile.readline()

arrCols=[]

for i in range(14):
    col=[]
    for j in range(294):
        col.append(arrRows[j][i])
    arrCols.append(col)

arrColsAvg=[]

for i in range(14):
    tot=0
    for j in range(294):
        if(arrCols[i][j]!='?'):
            tot=tot+float(arrCols[i][j])
    arrColsAvg.append(int(tot/295))

for i in range(14):
    for j in range(294):
        if(arrCols[i][j]=='?'):
            arrCols[i][j]=arrColsAvg[i]

for i in range(14):
    for j in range(294):
        sheet1.write(j+1,i,arrCols[i][j])


#Essential to save the work
workbook.close()