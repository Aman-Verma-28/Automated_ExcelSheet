import openpyxl

# opening the workbook 
#pass the path to your excel sheet here as the string

wb=openpyxl.load_workbook("C:/Users/verma/OneDrive/Desktop/Mysheet.xlsx")


#if there are multiple sheets in the file then open the sheet you want to work on
sh1=wb['Sheet4']

#for accessing a particular row change the value of row and col till where you want to read to

row=1 # to read the row number
col=10 # to read upto that column number

for i in range(1,col+1):
    dataInCell=sh1.cell(i,row).value
    if dataInCell!=None:
        print(dataInCell)
    # now you can process this data in whichever manner you want
