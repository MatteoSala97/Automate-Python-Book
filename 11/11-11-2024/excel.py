import openpyxl
import os

filepath = r'C:\Users\matteo.sala\Documents\Automate Python Book\11\11-11-2024\tabella.xlsx'

wb = openpyxl.load_workbook(filepath)

sheet = wb['Foglio 1']

# for row in sheet.iter_rows(values_only=True):
#     print(row)
print(sheet['A14'].value)
sheet['A14'] = 'Romus' 
print(sheet['A14'].value)

wb.save(filepath)
os.startfile(filepath)