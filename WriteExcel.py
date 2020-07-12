import openpyxl

path = r"C:\Users\PawelGilecki\Desktop\SeleniumTest\Test1.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook["Arkusz1"]

for r in range(1, 5):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value="welcome"

workbook.save(path)